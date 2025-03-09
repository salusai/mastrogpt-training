import sys, pathlib, base64
sys.path.append("packages/vision/store")
import bucket, vision
import base64

def test_store():
    buc = bucket.Bucket({})
    assert len(buc.find("cat")) == 0
    body = pathlib.Path("tests/vision/cat.jpg").read_bytes()
    buc.write("cat.jpg", body)
    ls = buc.find("cat")
    assert len(ls) == 1
    sz =  buc.size(ls[0])
    assert sz > 0
<<<<<<< HEAD
    b64 = buc.read(ls[0])
    assert len(b64) >= sz
    vis = vision.Vision({})
    res = vis.decode(base64.b64encode(b64).decode("utf-8"))
=======
    file = buc.read(ls[0])
    assert len(file) == sz
    vis = vision.Vision({})
    b64 = base64.b64encode(file).decode()
    res = vis.decode(b64)
>>>>>>> abf6e5c (vdb)
    assert res.find("cat") != -1
    n = buc.remove(ls[0])
    assert n == 1
    assert len(buc.find("cat")) == 0
