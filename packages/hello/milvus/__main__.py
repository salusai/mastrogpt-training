#--kind python:default
#--web true
import milvus
def main(args):
  return { "body": milvus.milvus(args) }
