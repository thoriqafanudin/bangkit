import os
import csv

nama = input("Masukan nama\t: ")
nim = input("Masukan nim\t: ")
nama_file = nim + ".txt"

def menyimpan_data(nama_file, nama, nim):
    os.chdir("new_dir")
    file = open(nama_file, "w")
    file.write(f"{nama},{nim}")
    file.close()
    
menyimpan_data(nama_file, nama, nim)
print(f"data {nama} dengan nim {nim} berhasil dibuat pada file {nama_file}")
os.chdir("..")
data_mhs = os.listdir("new_dir")
os.chdir("new_dir")
for data in data_mhs:
    file = open(data, "r")
    file_str = file.read()
    file_split = file_str.split(",")
    print(f"{file_split[0]}\t\t{file_split[1]}")
    
    file.close()