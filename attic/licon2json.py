import sys
from pathlib import Path
import csv
import json

if len(sys.argv) < 2:
    print("please specify the path of a Linkedin Connections.csv file")
    sys.exit(0)

#filein = "Connections.csv"
filein = sys.argv[1]
fileout = filein.rsplit(".",1)[0] + ".json"

#file = open(filein)
with open(filein) as file:

    #lines = Path(filein).read_text().split("\n")
    reader = csv.reader(file)
    # skip empty lines
    next(reader) ; next(reader) ; next(reader)
    header = next(reader)
    res = ""
    count = 0
    for line in reader:
        try:
            [name, surname, url, email, company, job, connected] = line
            if name + surname == "": 
                continue
        except:
            print("\nskip", line)
            continue
        m = {}
        m["name"] = f"{name} {surname}"
        if email: m["email"] = email
        if company: m["company"] = company
        if job: m["job"] = job
        if url: m["linkedin"] = url.split("/")[-1]
        sent = json.dumps(m)
        print(".", end='')
        res += sent+"\n"
        count += 1
        if count % 100 == 0: print() ; print(count, end='')
 
Path(fileout).write_text(res)
print(f"\n*** saved {fileout}")


   