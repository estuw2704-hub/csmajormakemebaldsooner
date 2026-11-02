import os
os.system('cls')

from abc import ABC, abstractmethod

class Kendaraan(ABC):
    def __init__(self, plat_nomor, tarif_dasar):
        self.__plat_nomor = plat_nomor
        self.tarif_dasar = tarif_dasar

    @property
    def plat_nomor(self):
        return self.__plat_nomor

    @abstractmethod
    def hitung_biaya_sewa(self, lama_hari):
        pass

class Motor(Kendaraan):

    jenis = "Motor"

    def hitung_biaya_sewa(self, lama_hari):
        return self.tarif_dasar * lama_hari

class Mobil(Kendaraan):

    jenis = "Mobil"

    def hitung_biaya_sewa(self, lama_hari):
        return (self.tarif_dasar * lama_hari) + 50000

motor1 = Motor("B1234XYZ", 30000)
mobil1 = Mobil("B5678ABC", 120000)

daftar_kendaraan = [motor1, mobil1]

for kendaraan in daftar_kendaraan:
    biaya = kendaraan.hitung_biaya_sewa(3)
    biaya_rapi = f"{biaya:,}".replace(",", ".")

    print(kendaraan.plat_nomor, "-", kendaraan.jenis, "-> Rp", biaya_rapi)