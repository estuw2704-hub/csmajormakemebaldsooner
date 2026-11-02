presensi = [
    "2513020001", "2513020005", "2513020012",
    "2513020018", "2513020023", "2513020031",
    "2513020040"
]

def sequential_search(data, target):
    diperiksa = 0

    for i in range(len(data)):
        diperiksa += 1
        if data[i] == target:
            return i, diperiksa

    return -1, diperiksa


nim = input("masukkan nim yang dicari: ")
posisi, diperiksa = sequential_search(presensi, nim)

if posisi != -1:
    print(f"nim {nim} hadir, tercatat di urutan ke-{posisi + 1} (index {posisi})")
else:
    print(f"nim {nim} tidak terdaftar dalam presensi")

print(f"jumlah data yang diperiksa: {diperiksa}")