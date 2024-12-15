#--kind python:default
#--web true
import postgen
def main(args):
  return {"body": postgen.postgen(args)}
