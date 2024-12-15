#--kind python:default
#--web true
import querydoc
def main(args):
  return {"body": querydoc.querydoc(args)}
