import csv

# membaca csv dalam bentuk dictionary
with open("hosts.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        
# write csv dengan dictionary
users = [{"name":"Thoriq Afanudin", "username":"afan", "department":"IT Consultan"},
{"name":"Ummu Fitrotin", "username":"ummu", "department":"Data Analys"}]

keys = ["name", "username", "department"]

with open("users.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)