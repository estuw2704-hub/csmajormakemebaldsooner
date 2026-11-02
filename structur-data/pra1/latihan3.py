# latihan 3 - ADT stack dengan List (tumpukan piring)
import os
os.system('cls')

tumpukan = []


def is_empty():
    return len(tumpukan) == 0


def push(item):
    tumpukan.append(item)


def pop():
    return tumpukan.pop() if not is_empty() else None


def peek():
    return tumpukan[-1] if not is_empty() else None


# tumpuk tiga piring                                            # jawaban soal reflektif nomor 2 <<==
push("piring a")                                                # contoh prinsip LIFO di kehidupan sehari-hari
push("piring b")                                                # tumpukan buku di meja, buku yang terakhir di taruh
push("piring c")                                                # paling atas, justru di ambil pertama kali dari yang bawahnya.

# pelayan mengambil piring paling atas
print(f"piring yang terambil pelayan: {pop()}")

# tambah piring baru
push("piring d")

# lihat piring paling atas tanpa mengambil
print(f"piring paling atas sekarang: {peek()}")

# ambil semua piring sampai kosong                              # jawaban soal reflektif nomor 1 <<==
print("mengambil semua piring:")                                # stack LIFO (last in, first out)  
while not is_empty():                                           # piring d dimasukkan paling akhir
    print(f"- {pop()}")                                         # sehingga keluar paling awal, sedangkan
print("tumpukan piring sudah kosong.")                          # piring a di dasar tumpukan keluar paling akhir.