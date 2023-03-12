import os

# menghapus file
os.remove("kalkulator.py")

# mengubah nama file
os.rename("kalkulator.py", "perhitungan.py")

# mengecek keberadaan file
print(os.path.exists("perhitungan.py"))

# mengetahui memori file dalam bytearray
print(os.path.getsize("perhitungan.py"))

# memperoleh waktu yang dimulai sejak 1 januari 1970
print(os.path.getmtime("perhitungan.py"))

# memperoleh date time, misalnya ingin tahu kapan file dibuat
import datetime
timestamp = os.path.getmtime("perhitungan.py")
print(datetime.datetime.fromtimestamp(timestamp))

# mengetahui letak direktori file
print(os.path.abspath("perhitungan.py"))

# mengetahui letak direktori bekerja
print(os.getcwd())

# membuat new direktori
os.mkdir("new_dir")

# berpindah diretori
os.chdir("new_dir")

# menghapus direktori
os.rmdir("new_dir")

# mengetahui isi direktori
print(os.listdir("new_dir"))

# mengecek/membedakan direktori atau file
print(os.path.isdir("new_dir"))

# it creates a string containing cross-platform concatenated directories
print(os.path.join("new_dir", "exampl.txt"))

'/home/student-04-841605dbcb28/data/employees.csv'

#!/usr/bin/env python3
import csv
def read_employees(csv_file_location):
    csv.register_dialect()