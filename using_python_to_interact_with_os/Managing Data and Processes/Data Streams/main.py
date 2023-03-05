def to_second(hour, minute, second):
    return hour*3600 + minute*60 + second
    
cont = "y"

while cont.lower() == "y":
    hour = int(input("Masukan jam\t: "))
    minute = int(input("Masukan menit\t: "))
    second = int(input("Masukan detik\t: "))
    total = to_second(hour, minute, second)
    print(f"{hour} jam + {minute} menit + {second} detik = {total} detik")
    
    is_done = input("Apakah Anda akan menghitung lagi? ")
    cont = is_done
    
print("SELAMAT, program selesai")

