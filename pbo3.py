from enum import Enum


class statuspesanan(Enum):
    menunggu = "menunggu"
    diproses = "diproses"
    selesai = "selesai"
    dibatalkan = "dibatalkan"


class user:
    def __init__(self, nama, username, password):
        self.nama = nama
        self.username = username
        self.password = password

    def login(self, username, password):
        return self.username == username and self.password == password


class menu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga


class detailpesanan:
    def __init__(self, menu, jumlah):
        self.menu = menu
        self.jumlah = jumlah

    def hitung_subtotal(self):
        return self.menu.harga * self.jumlah


class pesanan:
    def __init__(self):
        self.items = []
        self.total_harga = 0
        self.status = statuspesanan.menunggu

    def tambah_item(self, detail):
        self.items.append(detail)
        self.hitung_total()

    def hitung_total(self):
        self.total_harga = sum(d.hitung_subtotal() for d in self.items)
        return self.total_harga

    def batalkan(self):
        if self.status != statuspesanan.menunggu:
            return False
        self.status = statuspesanan.dibatalkan
        return True


class mahasiswa(user):
    def buat_pesanan(self):
        return pesanan()

    def batalkan_pesanan(self, pesanan):
        return pesanan.batalkan()


class pemilikkantin(user):
    def kelola_menu(self, menu):
        pass

    def update_status(self, pesanan, status):
        pesanan.status = status