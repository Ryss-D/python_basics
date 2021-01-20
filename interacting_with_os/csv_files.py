import csv

f = open("csv file")
csv_f = csv.reader(f)
for row in csv_f:
    name, phone, role = row
    print("name : {}, phone: {}, role:{}".format(name, phone, role))
f.close

hosts = [[1, 2],[3,4]]

with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(("{} has {} users").format(row["name"], row["users"]))

users = ["list of dictionarys"]
keys = ["list of columns"]
with open('software.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
