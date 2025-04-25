#--web true
import requests
def main(args):
     myip = requests.get("https://api.ipify.org?format=json").json() 
     return { "body": myip.get("ip", "unknown") }
