import os
import datetime

'''
first_name = "novel.txt"
last_name = "cerpen.txt"
os.rename(first_name, last_name)

os.remove("text_biasa.txt")

check = os.path.exists("cerpen.txt")
print(check)

size = os.path.getsize("cerpen.txt")
print(size)
'''
timestamp = os.path.getmtime("cerpen.txt")
tanggal = datetime.datetime.fromtimestamp(timestamp)
tgl = str(tanggal)
print(tgl[:10])
print(tgl[11:19])
print(type(tanggal))