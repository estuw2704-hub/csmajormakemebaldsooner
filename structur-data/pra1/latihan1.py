# latihan 1 - tipe data & konversi tipe (konversi suhu)
import os
os.system('cls')

suhu_teks = input("masukkan suhu (celsius): ")
 
try:
    celsius = float(suhu_teks)  # konversi eksplisit str -> float
except ValueError:
    print("input tidak valid hoy! masukkan angka..") # jawaban soal reflektif nomor 2 <<==
else:
    fahrenheit = celsius * 9 / 5 + 32
    kelvin = celsius + 273.15
 
    print(f"sebelum konversi: {suhu_teks!r} ({type(suhu_teks)})")
    print(f"sesudah konversi: {celsius} ({type(celsius)})")
    print(f"celsius   : {celsius:.2f} c")
    print(f"fahrenheit: {fahrenheit:.2f} f")
    print(f"kelvin    : {kelvin:.2f} k")

# jawaban soal reflektif nomor 1 <<==
# jika input "30.5" dikonversi dengan int(), program akan error
# (valueError) karena int() hanya menerima bilangan bulat.
# float dipilih karena suhu sering berupa bilangan desimal dan
# rumus kelvin (c + 273.15) juga menghasilkan desimal, sedangkan
# int tidak bisa menyimpan angka di belakang koma.
# jika pengguna mengetik koma ("30,5"), float() juga error, jadi
# koma perlu diganti titik dulu dengan .replace(",", ".").