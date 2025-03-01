import os, boto3, base64
from botocore.client import Config

class Bucket:
    def __init__(self, args):
        host = args.get("S3_HOST", os.getenv("S3_HOST"))
        port = args.get("S3_PORT", os.getenv("S3_PORT"))
        url = f"http://{host}:{port}"
        key = args.get("S3_ACCESS_KEY", os.getenv("S3_ACCESS_KEY"))
        sec = args.get("S3_SECRET_KEY", os.getenv("S3_SECRET_KEY"))
        cfg = Config(signature_version='s3v4')
        self.client = boto3.client('s3', region_name='us-east-1', endpoint_url=url, aws_access_key_id=key, aws_secret_access_key=sec)
        self.bucket = args.get("S3_BUCKET_DATA", os.getenv("S3_BUCKET_DATA"))
        
    def write(self, key, body):
        try:
          self.client.put_object(Bucket=self.bucket, Key=key, Body=body)
          return "OK" if self.size(key) != -1 else "Error"
        except Exception as e:
          return str(e)
        
    def read_b64(self, key):
      try:
        res = self.client.get_object(Bucket=self.bucket, Key=key)
        data = res["Body"].read()
        return base64.b64encode(data).decode("utf-8")
      except:
        return ""

    def size(self, key):
      try:
        status = self.client.head_object(Bucket=self.bucket, Key=key)
        size = status.get('ResponseMetadata', {}).get('HTTPHeaders', {}).get('content-length', -1)
        return int(size)
      except:
        return -1
    
    def find(self, sub):
      ls = []
      res = self.client.list_objects_v2(Bucket=self.bucket)
      if 'Contents' in res:
        for obj in res['Contents']:
          name = obj['Key']
          if name.find(sub) != -1:
            ls.append(name)
      return ls

    def remove(self, prefix):
      count = 0
      res = self.client.list_objects_v2(Bucket=self.bucket)
      if 'Contents' in res:
        for obj in res['Contents']:
          #obj = res['Contents'][0]
          key = obj['Key']
          if key.startswith(prefix):
            res = self.client.delete_object(Bucket=self.bucket, Key=key)
            count += 1
      return count

