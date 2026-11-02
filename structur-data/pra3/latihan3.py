rekam_medis = [
    1002, 1015, 1023, 1047, 1058, 1062, 1079, 1085,
    1091, 1104, 1118, 1125, 1137, 1149, 1156
]

def sudah_terurut(data):
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True


def binary_search(data, target):
    low = 0
    high = len(data) - 1
    langkah = 0

    while low <= high:
        mid = (low + high) // 2
        langkah += 1

        print(
            f"langkah {langkah}: low={low}, high={high}, "
            f"mid={mid}, data[mid]={data[mid]}"
        )

        if data[mid] == target:
            return mid, langkah
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, langkah


if sudah_terurut(rekam_medis):
    for nomor in [1118, 1050]:
        print(f"mencari rekam medis {nomor}:")
        posisi, langkah = binary_search(rekam_medis, nomor)

        if posisi != -1:
            print(f"ditemukan di index {posisi} setelah {langkah} langkah")
        else:
            print(f"rekam medis {nomor} tidak ditemukan setelah {langkah} langkah")

        print()
else:
    print("peringatan: data rekam medis belum terurut.")
    print("binary search tidak dapat dijalankan.")