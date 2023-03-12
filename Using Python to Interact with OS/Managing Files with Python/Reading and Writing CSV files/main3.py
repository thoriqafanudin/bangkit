with open("data_mhs.csv") as file:
    # membaca file keseluruhan
    #print(file.read())
    
    # membaca file satu baris
    #print(file.readline())
    
    # membaca file dalam bentuk list per row
    #print(file.readlines())
    
    # menghilangkan enter saat membaca file per baris (strip)
    for line in file:
        print(line.strip().upper())
        

# menulis file
with open("new_file.txt", "w") as file:
    file.write("Hello World")