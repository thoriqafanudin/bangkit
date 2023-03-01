import csv
name_file = "by_department.csv"
with open(name_file) as by_department:
    reader = csv.DictReader(by_department)
    for row in reader:
        print(f"name: {row['name']}\tnickname: {row['username']}\tdepartment: {row['department']}")