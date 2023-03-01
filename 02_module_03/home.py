print("SELAMAT DATANG DI APLIKASI")
print("-"*30)
print("Menu")
print("1. READ DATA USER")
print("2. CREATE DATA USER")
print("3. LOG IN")
print("-"*30)
pilihan = input("Masukan pilihan: ")
print("-"*30)
if pilihan == "1":
    import main6
elif pilihan == "2":
    import main7
elif pilihan == "3":
    import login
else:
    print("INPUT YANG ANDA MASUKAN SALAH")