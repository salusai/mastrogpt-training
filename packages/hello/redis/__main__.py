#--kind python:default
#--web true
import redis
def main(args):
  return { "body": redis.redis(args) }
