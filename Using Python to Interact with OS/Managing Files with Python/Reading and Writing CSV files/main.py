import csv

# membaca file csv
with open("data_mhs.csv") as file:
    csv_file = csv.reader(file)
    for row in csv_file:
        nama, nim, asal_daerah = row
        print(f"Nama: {nama}, Nim: {nim}, Daerah: {asal_daerah}")
        
        
# membuat file csv
hosts = [["indihome", "192.168.171.11"], ["localhost", "121.213.231.22"]]
with open("hosts.csv", "w") as hosts_file:
    writer = csv.writer(hosts_file)
    writer.writerows(hosts)