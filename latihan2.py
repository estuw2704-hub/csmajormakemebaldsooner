stok_barang = ["pensil", "buku", "penggaris", "pulpen"]
dicari = input("cari barang: ")

index_ketemu = -1
for i in range(len(stok_barang)):
    if stok_barang[i] == dicari:
        index_ketemu = i
        break

if index_ketemu != -1:
    print(f"ditemukan di index ke-{index_ketemu}")
else:
    print("barang tidak ditemukan")

if dicari in stok_barang:
    print(f"[in/index] ditemukan di index ke-{stok_barang.index(dicari)}")
else:
    print("[in/index] barang tidak ditemukan")
