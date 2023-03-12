#!/usr/bin/env python3
import re
import operator
import csv

file_log = "syslog.log"
with open(file_log) as f:
  list_error = []
  file = f.readlines()
  for line in file:
    error = re.findall(r"ticky: ERROR ([\w ']*) ", line)
    if len(error) != 0:
      list_error.append(error[0])

unix_error = []
for unix in list_error:
  if not unix in unix_error:
    unix_error.append(unix)
daftar_hitung = []
for unix in unix_error:
  hitung = list_error.count(unix)
  daftar_hitung.append(hitung)
dict_jumlah_error = {}
i = 0
for unix in unix_error:
  dict_jumlah_error[unix] = daftar_hitung[i]
  i += 1
error_urut = sorted(dict_jumlah_error.items(), key = operator.itemgetter(1), reverse=True)
ket_err = []
ket_jum = []
for data in error_urut:
  error, jumlah = data
  ket_err.append(error)
  ket_jum.append(jumlah)
my_dict = {
    "Error": ket_err,
    "Count": ket_jum,
}

with open("report_error.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(my_dict.keys())
    writer.writerows(zip(*my_dict.values()))

daftar_nama = []

regex = r"\([\w\.]*\)"

with open(file_log) as f:
  list_error = []
  daftar_info = []
  daftar_error_semua = []
  file = f.readlines()
  for error in file:
    result = re.findall(regex, error)
    if len(result) != 0:
      tambah = result[0]
      daftar_nama.append(tambah[1:-1])
    result_2 = re.findall("INFO", error)
    if len(result_2) != 0:
      daftar_info.append(result_2[0])
    result_3 = re.findall("ERROR", error)
    if len(result_3) != 0:
      daftar_error_semua.append(result_3[0])
nama_unix = []
for nama in daftar_nama:
  if not nama in nama_unix:
    nama_unix.append(nama)

# nama_unix, daftar_info, daftar_error_semua