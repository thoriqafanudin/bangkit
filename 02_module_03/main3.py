import csv

users = [{"name":"Thoriq", "username":"thor", "department":"IT infrasturcture"},
{"name":"Faisa Nirbita", "username":"faisa", "department":"Human resource"},
{"name":"Ummu Fitrotin", "username":"ummu", "department":"HRD"}]

keys = ["name", "username", "department"]
file_name = "by_department.csv"
with open(file_name, "w") as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
    
print(f"File dengan nama {file_name} berhasil dibuat")