import os, boto3
from botocore.client import Config

def connect(args):
    host = args.get("S3_HOST", os.getenv("S3_HOST"))
    port = args.get("S3_PORT", os.getenv("S3_PORT"))
    url = f"http://{host}:{port}"
    key = args.get("S3_ACCESS_KEY", os.getenv("S3_ACCESS_KEY"))
    sec = args.get("S3_SECRET_KEY", os.getenv("S3_SECRET_KEY"))
    cfg = Config(signature_version='s3v4')
    #s3 = boto3.resource('s3', config=cfg, region_name='us-east-1',
    #      endpoint_url=url, aws_access_key_id=key, aws_secret_access_key=sec)
    s3 = boto3.client('s3', region_name='us-east-1', endpoint_url=url, aws_access_key_id=key, aws_secret_access_key=sec )

    bucket =args.get("S3_BUCKET_DATA", os.getenv("S3_BUCKET_DATA"))
    return (s3, bucket)
      
def write(s3, bucket, filecontent):
  try:
    [key, body] = filecontent.split("=", maxsplit=1)
    s3.put_object(Bucket=bucket, Key=key, Body=body)
    return check(s3, bucket, key)
  except:
    return "please separate file from content with '='"

def check(s3, bucket, key):
  try:
    status = s3.head_object(Bucket=bucket, Key=key)
    size = status.get('ResponseMetadata', {}).get('HTTPHeaders', {}).get('content-length', -1)
    return f"{key} size {size}"
  except:
    return f"{key} not found"
    
def show(s3, bucket, sub):
  out = f"Objects in {bucket} with substring '{sub}':\n"
  res = s3.list_objects_v2(Bucket=bucket)
  if 'Contents' in res:
    for obj in res['Contents']:
      name = obj['Key']
      if name.find(sub) != -1:
        out += f"- {name}\n"
  return out

def remove(s3, bucket, prefix):
  if prefix == "":
    return "please provide a not empty prefix"
  out = f"Removed objects in {bucket} with prefix '{prefix}':\n"
  res = s3.list_objects_v2(Bucket=bucket)
  if 'Contents' in res:
    for obj in res['Contents']:
      #obj = res['Contents'][0]
      key = obj['Key']
      if key.startswith(prefix):
        res = s3.delete_object(Bucket=bucket, Key=key)
        out += f"- removed {key}\n"
  return out

def store(args):
  inp = args.get("input", "")
  out = """
usage:
  @<file>       upload a local <file>
  *<substring>  list files with <subtring> in path
  !<prefix>     remove files starting with <prefix>
  ><file>=<content> create a <file> with <content>
"""
  (s3, bucket) = connect(args)
  if inp.startswith("@"):
    out = check(s3, bucket, inp[1:])
  elif inp.startswith("*"):
    out = show(s3, bucket, inp[1:])
  elif inp.startswith("!"):
    out = remove(s3, bucket, inp[1:])
  elif inp.startswith(">"):
    out = write(s3, bucket, inp[1:])
    
  return {"output": out}
