import os, requests as req
import base64, pathlib, boto3
import vision
from vision.store.bucket import Bucket
from datetime import datetime

USAGE = "Please upload a picture and I will tell you what I see"
FORM = [
  {
    "label": "any pics?",
    "name": "pic",
    "required": "true",
    "type": "file"
  },
]

def form(args):
  res = {}
  out = USAGE
  inp = args.get("input", "")

  if type(inp) is dict and "form" in inp:
    img = inp.get("form", {}).get("pic", "")
    print(f"uploaded size {len(img)}")
    # decode image
    vis = vision.Vision(args)
    out = vis.decode(img)
    # upload to S3
    ## setup the bucket
    s3bucket = Bucket(args)
    ## define image key and write the file
    image_key = "file_" + datetime.now().strftime("%Y%m%d_%H%M%S%f")+".jpg"
    s3bucket.write(image_key, out)
    # read the file from s3
    img_url = s3bucket.exturl(image_key, 3600)
    # return external link to image
    res['html'] = f'<img src="{img_url}">'
    
  res['form'] = FORM
  res['output'] = out
  return res
