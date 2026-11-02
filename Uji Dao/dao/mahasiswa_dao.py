from abc import ABC, abstractmethod
from typing import List, Optional

from models.mahasiswa import Mahasiswa


class MahasiswaDAO(ABC):
    @abstractmethod
    def insert(self, m: Mahasiswa) -> None: ...

    @abstractmethod
    def update(self, m: Mahasiswa) -> None: ...

    @abstractmethod
    def delete(self, nim: str) -> None: ...

    @abstractmethod
    def find_by_id(self, nim: str) -> Optional[Mahasiswa]: ...

    @abstractmethod
    def find_all(self) -> List[Mahasiswa]: ...