import os
import csv

nama_file = "users.txt"

def membuat_file_user(nama_file):
    file = open(nama_file, 'w')
    file.write("Thoriq Afanudin,afan03@gmail.com,9865gjgdAQ\n")
    file.close()
    
def menambahkan_user(nama_file, nama, email, password):
    file = open(nama_file, 'a')
    file.write(f"{nama},{email},{password}\n")
    file.close()
    
def menampilkan_data_user(nama_file):
    file = open(nama_file, 'r')
    list_users = file.readlines()
    for i in list_users:
        split_data = i.split(',')
        nama = split_data[0]
        email = split_data[1]
        password = split_data[2]
        password = password[:-1]
        print("{:<20}{:<30}{:<20}".format(nama, email, password))
    file.close()

def login(email, password):
    file = open(nama_file, 'r')
    list_users = file.readlines()
    bool_email = False
    bool_password = False
    string_gagal = ""
    for user in list_users:
        split_data = user.split(',')
        email_tersimpan = split_data[1]
        
        if email != email_tersimpan:
            continue
        elif email == email_tersimpan:
            bool_email = True
            break
        
    for user in list_users:
        split_data = user.split(',')
        password_tersimpan = split_data[2]
        password_tersimpan = password_tersimpan[:-1]
        
        if password != password_tersimpan:
            continue
        elif password == password_tersimpan:
            bool_password = True
            break
    
    file.close()
    
    if not bool_email:
        print("EMAIL YANG ANDA MASUKAN SALAH")
    
    if not bool_password:
        print("PASSWORD YANG ANDA MASUKAN SALLAH")
    
    if bool_email and bool_password:
        print("LOGIN BERHASIL")
    else:
        print("LOGIN GAGALLLL!")