import os,pymilvus
from pymilvus import MilvusClient, DataType

url = f"http://{os.getenv("MILVUS_HOST")}"
token = os.getenv("MILVUS_TOKEN")
db_name = os.getenv("MILVUS_DB_NAME")

client = MilvusClient(uri=url, token=token, db_name=db_name)

client.list_collections()
client.drop_collection("test")

COLLECTION="test"
DIMENSION=1024

schema = client.create_schema()
schema.add_field("id", datatype=DataType.INT64, is_primary=True, auto_id=True)
schema.add_field("text", datatype=DataType.VARCHAR, length=DIMENSION)
schema.add_field("embeddings", datatype=DataType.FLOAT_VECTOR, dim=DIMENSION)

index_params = client.prepare_index_params()
index_params.add_index("embeddings", index_type="AUTOINDEX", metric_type="IP")

client.create_collection(collection_name=COLLECTION,
                         schema=schema, index_params=index_params)

text = "Hello world"
vec = [float(i) for i in range(0,DIMENSION)]
client.insert(COLLECTION,{"text": text, "embeddings": vec})

qit = client.query_iterator(collection_name=COLLECTION, batch_size=2, output_fields=["text"])
res = qit.next()
print(res[0].get("text"))