import math

print("PROGRAM LINGKARAN")
print("1. menghitung luas lingkaran")
print("2. menghitung keliling lingkaran")

pilihan = int(input("masukkan pilihan(1/2): "))
r = float(input("masukkan jari-jari lingkaran: "))
if pilihan == 1 :
    keliling = 2* math.pi * r
    print("keliling lingkaran adalah: ", keliling)
elif pilihan == 2 :
    luas = math.pi * r * r
    print("luas lingkaran adalah: ", luas)
else :
    print("pilihan tidak tersedia!")
    