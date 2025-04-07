import sys
from pathlib import Path

#filein = "Connections.csv"
filein = sys.argv[1]

fileout = filein.rsplit(".",1)[0] + ".grp.txt"
lines = Path(filein).read_text().split("\n")

companies = {}

#line = lines[4]
for line in lines[4:]:
    counter = ""
    try:
        [name, surname, url, email, company, job, connected] = line.split(",")
        if name + surname == "": 
            continue

        if company == "": company = "NO-COMPANY"

        user = f"{name} {surname}"
        user += email if email else ""
        user += f", {job}" if job else ""
        user += f" {url}" if url else ""

        users = companies.get(company, [])
        users.append(user)
        companies[company] = user
    except:
        print("skip", line)
        continue


ls = companies.keys()
for company in ls:
    users = companies.get(company)
    print(company, len(users))

print(len(ls))