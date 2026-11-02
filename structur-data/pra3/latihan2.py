parkir = [
    "AG1234AB", "AG5678CD", "L9012EF", "AG3456GH",
    "N7890IJ", "AG1111KL", "B2222MN", "AG9999OP"
]

def seq_tanpa_sentinel(data, target):
    i = 0
    perbandingan = 0

    while True:
        perbandingan += 1

        if i >= len(data):
            return -1, perbandingan

        perbandingan += 1

        if data[i] == target:
            return i, perbandingan

        i += 1


def seq_dengan_sentinel(data, target):
    panjang_asli = len(data)
    data.append(target)
    i = 0
    perbandingan = 0

    while True:
        perbandingan += 1

        if data[i] == target:
            break

        i += 1

    data.pop()

    if i == panjang_asli:
        return -1, perbandingan

    return i, perbandingan


for plat in ["AG1111KL", "AG0000ZZ"]:
    posisi1, cek1 = seq_tanpa_sentinel(parkir, plat)
    posisi2, cek2 = seq_dengan_sentinel(parkir, plat)

    if posisi1 != -1:
        print(f"plat {plat}: terdaftar di index {posisi1}")
    else:
        print(f"plat {plat}: bukan pelanggan langganan")

    print(f"  tanpa sentinel : {cek1} perbandingan")
    print(f"  dengan sentinel: {cek2} perbandingan")

print(f"jumlah data setelah pencarian: {len(parkir)}")