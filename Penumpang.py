penumpang = ["William", "Kate", "Anderson", "Jame", "Mady"]

print("a. Daftar penumpang awal:")
print(penumpang)

penumpang.append("Jones")
print("\nb. Setelah Jones ditambahkan:")
print(penumpang)

penumpang[2] = "Grace"
print("\nc. Setelah Anderson diganti Grace:")
print(penumpang)

print("\nd. Apakah Thompson ada dalam daftar?")
print("Thompson" in penumpang)

penumpang.sort()
print("\ne. Daftar penumpang setelah diurutkan:")
print(penumpang)

print("\nf. Daftar 6 penumpang yang sampai di Yogyakarta:")
for nama in penumpang:
    print(nama)

penumpang.clear()
print("\ng. Daftar penumpang setelah dikosongkan:")
print(penumpang)
