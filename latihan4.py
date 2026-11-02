nilai_matkul = [
    [80, 90, 70],
    [85, 75, 95],
    [60, 88, 92],
]

for baris in nilai_matkul:
    for nilai in baris:
        print(nilai, end=" ")
    print()

print("nilai_matkul[1][2] =", nilai_matkul[1][2])

nilai_matkul[0][0] = 85
print("setelah update [0][0]:", nilai_matkul[0])

nilai_matkul.append([78, 82, 90])
print("setelah tambah baris:", nilai_matkul)

def rata_rata_baris(matriks, baris):
    total = 0
    for nilai in matriks[baris]:
        total = total + nilai
    return total / len(matriks[baris])

for i in range(len(nilai_matkul)):
    print(f"rata-rata mahasiswa {i}: {rata_rata_baris(nilai_matkul, i)}")
