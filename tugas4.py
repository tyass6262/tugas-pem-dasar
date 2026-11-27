hari_pertama = {"keju", "tepung", "garam", "gula", "coklat"}
hari_kedua = {"garam", "gula", "coklat", "kecap"}

print("a. Set pembelian hari pertama:", hari_pertama)
print("   Set pembelian hari kedua:", hari_kedua)

hari_kedua.add("keju")
print("\nb. Setelah menambahkan keju:", hari_kedua)

barang_sama = hari_pertama.intersection(hari_kedua)
print("\nc. Barang yang sama:", barang_sama)

barang_hanya_hari_pertama = hari_pertama.difference(hari_kedua)
print("\nd. Barang hanya hari pertama:", barang_hanya_hari_pertama)

hari_pertama.discard("garam")
print("\ne. Setelah menghapus garam:", hari_pertama)

barang_hanya_hari_kedua = hari_kedua.difference(hari_pertama)
print("\nf. Barang hanya hari kedua:", barang_hanya_hari_kedua)

barang_tidak_sama = hari_pertama.symmetric_difference(hari_kedua)
print("\ng. Barang yang tidak sama:", barang_tidak_sama)

print("\nh. Semua pembelian hari pertama:", hari_pertama)

print("\ni. Semua pembelian hari kedua:", hari_kedua)
