def tukar(data, a, b):
    temp = data[a]
    data[a] = data[b]
    data[b] = temp


def bubble_sort(data, naik):
    n = len(data)
    perbandingan = 0
    tukar_count = 0

    for i in range(1, n):
        ada_tukar = False

        for j in range(0, n - i):
            perbandingan += 1

            if (naik and data[j] > data[j + 1]) or (not naik and data[j] < data[j + 1]):
                tukar(data, j, j + 1)
                tukar_count += 1
                ada_tukar = True

        print(f"Proses {i}: {data}")

        if not ada_tukar:
            break

    return perbandingan, tukar_count


def exchange_sort(data, naik):
    n = len(data)
    perbandingan = 0
    tukar_count = 0
    proses = 1

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            perbandingan += 1

            if (naik and data[i] > data[j]) or (not naik and data[i] < data[j]):
                tukar(data, i, j)
                tukar_count += 1

        print(f"Proses {proses}: {data}")
        proses += 1

    return perbandingan, tukar_count


def selection_sort(data, naik):
    n = len(data)
    perbandingan = 0
    tukar_count = 0
    proses = 1

    for i in range(0, n - 1):
        pos = i

        for j in range(i + 1, n):
            perbandingan += 1

            if (naik and data[j] < data[pos]) or (not naik and data[j] > data[pos]):
                pos = j

        if pos != i:
            tukar(data, pos, i)
            tukar_count += 1

        print(f"Proses {proses}: {data}")
        proses += 1

    return perbandingan, tukar_count


def insertion_sort(data, naik):
    n = len(data)
    perbandingan = 0
    geser_count = 0
    proses = 1

    for i in range(1, n):
        temp = data[i]
        j = i - 1

        while j >= 0:
            perbandingan += 1

            if (naik and data[j] > temp) or (not naik and data[j] < temp):
                data[j + 1] = data[j]
                geser_count += 1
                j -= 1
            else:
                break

        data[j + 1] = temp

        print(f"Proses {proses}: {data}")
        proses += 1

    return perbandingan, geser_count


while True:
    print("\n=== MENU SORTING ===")
    print("1. Bubble Sort")
    print("2. Exchange Sort")
    print("3. Selection Sort")
    print("4. Insertion Sort")
    print("0. Keluar")

    pilihan = input("Pilih metode: ")

    if pilihan == "0":
        print("Program selesai.")
        break

    if pilihan not in ["1", "2", "3", "4"]:
        print("Pilihan tidak valid.")
        continue

    data_input = input("Masukkan data dipisahkan spasi: ")

    try:
        data = [int(x) for x in data_input.split()]
    except ValueError:
        print("Data harus berupa angka.")
        continue

    if len(data) < 2:
        print("Masukkan minimal 2 data.")
        continue

    print("\n1. Urut Naik")
    print("2. Urut Turun")

    urutan = input("Pilih urutan: ")

    if urutan == "1":
        naik = True
        nama_urutan = "Naik"
    elif urutan == "2":
        naik = False
        nama_urutan = "Turun"
    else:
        print("Pilihan urutan tidak valid.")
        continue

    print("\nData awal:", data)
    print("Urutan:", nama_urutan)

    if pilihan == "1":
        perbandingan, jumlah = bubble_sort(data, naik)
        jenis_jumlah = "Tukar"

    elif pilihan == "2":
        perbandingan, jumlah = exchange_sort(data, naik)
        jenis_jumlah = "Tukar"

    elif pilihan == "3":
        perbandingan, jumlah = selection_sort(data, naik)
        jenis_jumlah = "Tukar"

    else:
        perbandingan, jumlah = insertion_sort(data, naik)
        jenis_jumlah = "Geser"

    print("\nHasil akhir:", data)
    print("Jumlah perbandingan:", perbandingan)
    print(f"Jumlah {jenis_jumlah.lower()}:", jumlah)