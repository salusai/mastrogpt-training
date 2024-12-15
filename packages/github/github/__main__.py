#--kind python:default
#--web true
import github
def main(args):
  return {"body": github.github(args)}
