#--kind python:default
#--web true
import assistant
def main(args):
  return { "body": assistant.assistant(args) }
