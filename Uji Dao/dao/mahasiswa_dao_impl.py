from contextlib import closing
from typing import List, Optional

from dao.mahasiswa_dao import MahasiswaDAO
from models.mahasiswa import Mahasiswa
from util.database_connection import DatabaseConnection


class MahasiswaDAOImpl(MahasiswaDAO):

    def insert(self, m: Mahasiswa) -> None:
        sql = ("INSERT INTO mahasiswa (nim, nama, ipk) "
               "VALUES (%s, %s, %s)")
        with closing(DatabaseConnection.get_connection()) as conn:
            with closing(conn.cursor()) as cur:
                cur.execute(sql, (m.nim, m.nama, m.ipk))
                conn.commit()

    def update(self, m: Mahasiswa) -> None:
        sql = ("UPDATE mahasiswa SET "
               "nama = %s, ipk = %s "
               "WHERE nim = %s")
        with closing(DatabaseConnection.get_connection()) as conn:
            with closing(conn.cursor()) as cur:
                cur.execute(sql, (m.nama, m.ipk, m.nim))
                conn.commit()

    def delete(self, nim: str) -> None:
        sql = ("DELETE FROM mahasiswa "
               "WHERE nim = %s")
        with closing(DatabaseConnection.get_connection()) as conn:
            with closing(conn.cursor()) as cur:
                cur.execute(sql, (nim,))
                conn.commit()

    def find_by_id(self, nim: str) -> Optional[Mahasiswa]:
        sql = "SELECT nim, nama, ipk FROM mahasiswa WHERE nim = %s"
        with closing(DatabaseConnection.get_connection()) as conn:
            with closing(conn.cursor()) as cur:
                cur.execute(sql, (nim,))
                row = cur.fetchone()
                if row is None:
                    return None
                return Mahasiswa(row[0], row[1], float(row[2]))

    def find_all(self) -> List[Mahasiswa]:
        sql = "SELECT nim, nama, ipk FROM mahasiswa"
        with closing(DatabaseConnection.get_connection()) as conn:
            with closing(conn.cursor()) as cur:
                cur.execute(sql)
                return [Mahasiswa(nim, nama, float(ipk))
                        for (nim, nama, ipk) in cur.fetchall()]