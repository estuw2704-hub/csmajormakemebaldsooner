from dao.mahasiswa_dao_impl import MahasiswaDAOImpl
from models.mahasiswa import Mahasiswa


def main():
    dao = MahasiswaDAOImpl()

    dao.insert(Mahasiswa("2201001", "Andi", 3.5))
    for m in dao.find_all():
        print(f"{m.nim} - {m.nama}")

    dao.update(Mahasiswa("2201001", "Andi P", 3.7))
    print(dao.find_by_id("2201001"))

    dao.delete("2201001")


if __name__ == "__main__":
    main()