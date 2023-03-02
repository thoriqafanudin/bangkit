import csv

mahasiswa = [{"nama":"Ika Widyaningrum", "nim":"2100006111", "prodi":"Pend. Matematika"},
{"nama":"Azizah Nurul", "nim":"1900006112", "prodi":"Pend. Bahasa Inggris"},
{"nama":"Rasyida Faiz", "nim":"1700006224", "prodi":"Teknik Industri"},
{"nama":"Ayu Wahyuni", "nim":"1600009212", "prodi":"Pend. Kedokteran"}]
keys = ["nama", "nim", "prodi"]
file = open("daftar_mhs.csv", "w")
writer = csv.DictWriter(file, fieldnames=keys)
writer.writeheader()
writer.writerows(mahasiswa)
print("DATA CSV BERHASIL DIBUAT")
file.close()