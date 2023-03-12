import re


data_error = ["ERROR: Gagal Login (toriq)",
"ERROR: Password Salah (ummu)",
"ERROR: Usename Salah (faisa)",
"INFO: Login Berhasil (faisa)",
"ERROR: Password Salah (fitrotin)"]

filtering = "ERROR: ([\w ]*) \([\w ]*\)"
filter_2 = r"\(([\w ]*)\)"
daftar_unix = []
daftar_hitung = []
daftar_all = []
for line in data_error:
    cari = re.search(filtering, line)
    if cari != None:
        print(cari[1])
        daftar_all.append(cari[1])
        if not cari[1] in daftar_unix:
            daftar_unix.append(cari[1])
            
for unix in daftar_unix:
    hitung = daftar_all.count(unix)
    daftar_hitung.append(hitung)
    
message_count_error = {}
i = 0
for unix in daftar_unix:
    message_count_error[unix] = daftar_hitung[i]
    i += 1
print(message_count_error)
import operator
result = sorted(message_count_error.items(), key=operator.itemgetter(1))

error = []
count = []
for i in range(len(daftar_unix)):
    err, cou = result[i]
    error.append(err)
    count.append(cou)

import csv

my_dict = {
    "Error": error,
    "Count": count,
}

with open("my_dict.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(my_dict.keys())
    writer.writerows(zip(*my_dict.values()))


      
