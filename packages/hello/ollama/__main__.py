#--kind python:default
#--web true
import ollama
def main(args):
  return { "body": ollama.ollama(args) }
