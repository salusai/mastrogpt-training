#--kind python:default
#--web true

import rag
def main(args):
  return { "body": rag.rag(args) }
