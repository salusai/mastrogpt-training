#--kind python:default
#--web true
import sitenav
def main(args):
  return {"body": sitenav.sitenav(args)}
