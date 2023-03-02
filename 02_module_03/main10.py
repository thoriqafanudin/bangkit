import csv
nama_file = "daftar_mhs.csv"
file = open(nama_file)
reader = csv.DictReader(file)
no = 1
for row in reader:
    nama = row["nama"]
    nim = row["nim"]
    prodi = row["prodi"]
    print("{}. {:<20}{:<15}{:<20}".format(no, nama, nim, prodi))
    no += 1
    
file.close()