anggota = list(range(10001, 12001, 2))


def sequential_search(data, target):
    perbandingan = 0

    for i, nomor in enumerate(data):
        perbandingan += 1

        if nomor == target:
            return i, perbandingan

    return -1, perbandingan


def binary_search(data, target):
    low = 0
    high = len(data) - 1
    perbandingan = 0

    while low <= high:
        mid = (low + high) // 2
        perbandingan += 1

        if data[mid] == target:
            return mid, perbandingan
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, perbandingan


print(f"jumlah anggota koperasi: {len(anggota)}")

for nomor in [11501, 10002]:
    posisi_seq, cek_seq = sequential_search(anggota, nomor)
    posisi_bin, cek_bin = binary_search(anggota, nomor)

    if posisi_seq != -1:
        print(f"nomor {nomor}: ditemukan di index {posisi_seq}")
    else:
        print(f"nomor {nomor}: tidak terdaftar")

    print(f"  sequential search: {cek_seq} perbandingan")
    print(f"  binary search    : {cek_bin} perbandingan")

print("kesimpulan: binary search lebih efisien untuk data besar yang sudah terurut.")