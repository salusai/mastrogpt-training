#--kind python:default
#--web true
import webrag
def main(args):
  return { "body": webrag.webrag(args) }
