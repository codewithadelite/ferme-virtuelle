from typing import List

from .culture import Culture
from .animal import Animal


class Ferme:
    def __init__(self, argent: int, espace: int):
        self.__argent: int = argent
        self.__espace: int = espace
        self.cultures: List[Culture] = []
        self.animaux: List[Animal] = []

    @property
    def argent(self) -> int:
        return self.__argent

    @property
    def espace(self) -> int:
        return self.__espace

