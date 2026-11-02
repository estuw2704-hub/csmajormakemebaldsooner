# latihan 4 - basis data sederhana (list of dict) toko tanaman hias
import os
os.system('cls')

produk = []

# create 4 produk                                                         # jawaban soal reflektif nomor 2 <<==
produk.append({"nama": "monstera", "harga": 150000})                      # setiap dict produk ditambah kunci "stok", misalnya
produk.append({"nama": "aglaonema", "harga": 85000})                      # {"nama": "Monstera", "harga": 150000, "stok": 3}.
produk.append({"nama": "sirih gading", "harga": 35000})                   # lalu fungsi total_nilai_stok() diubah agar menjumlahkan
produk.append({"nama": "kaktus mini", "harga": 25000})                    # harga x stok untuk tiap produk: total += p["harga"] * p["stok"].


def tampilkan(daftar_produk):
    for p in daftar_produk:
        print(f"- {p['nama']}: Rp{p['harga']}")


def total_nilai_stok(daftar_produk):
    total = 0
    for p in daftar_produk:
        total += p["harga"]
    return total


# read semua produk
print("daftar produk:")
tampilkan(produk)

# cari termahal secara manual (tanpa max())                               # jawaban soal reflektif nomor 1 <<==
termahal = produk[0]                                                      # Memahami cara kerja algoritma
for p in produk:                                                          # dan perbandingan di balik max() 
    if p["harga"] > termahal["harga"]:                                    
        termahal = p
print(f"produk termahal: {termahal['nama']} (Rp{termahal['harga']})")

# update harga aglaonema jadi 95000
produk[1]["harga"] = 95000

# delete: hapus monstera (index 0)
produk.pop(0)

print("setelah update & hapus:")
tampilkan(produk)

print(f"total nilai stok: Rp{total_nilai_stok(produk)}")