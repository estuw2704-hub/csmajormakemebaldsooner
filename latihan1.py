nilai_ujian = [80, 75, 90, 65, 88, 70]

for i in range(len(nilai_ujian)):
    print(f"index {i}: {nilai_ujian[i]}")

total = 0
for n in nilai_ujian:
    total = total + n
rata_rata = total / len(nilai_ujian)

tertinggi = nilai_ujian[0]
terendah = nilai_ujian[0]
for n in nilai_ujian:
    if n > tertinggi:
        tertinggi = n
    if n < terendah:
        terendah = n

print("total:", total)
print("rata-rata:", rata_rata)
print("tertinggi:", tertinggi)
print("terendah:", terendah)

print("verifikasi sum():", sum(nilai_ujian))
print("verifikasi rata-rata:", sum(nilai_ujian) / len(nilai_ujian))
