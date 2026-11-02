# latihan 2 - operasi CRUD pada List (antrean apotek)
import os
os.system('cls')

antrean = []

# create: 4 pelanggan lewat perulangan                          # jawaban soal reflektif nomor 1 <<==
for i in range(1, 5):                                           # perulangan lebih ringkas, mudah diubah jumlahnya
    nama = input(f"masukkan nama pelanggan ke-{i}: ")           # cukup ganti range, dan tidak mengulang kode yang sama.
    antrean.append(nama)

# read: tampilkan antrean beserta nomor urut
print("antrean awal:")
for no, nama in enumerate(antrean, start=1):
    print(f"{no}. {nama}")

# update: pelanggan urutan ke-2 diganti (index 1)
pengganti = "nategurs"
antrean[1] = pengganti
print(f"pelanggan urutan ke-2 digantikan oleh: {pengganti}")

# delete: pelanggan pertama selesai dilayani                    # jawaban soal reflektif nomor 2 <<==
selesai = antrean.pop(0)                                        # kalau pelanggan yang selesai bukan yang pertama, pop(0) tidak cocok
print(f"pelanggan yang selesai dilayani: {selesai}")            # pake remove(nama) atau pop(index) dengan posisi yang benar.

# read: sisa antrean
print("sisa antrean:")
for no, nama in enumerate(antrean, start=1):
    print(f"{no}. {nama}")