from abc import ABC, abstractmethod
from ..enumerations import AnimauxEnum, GrainesEnum


class AbastractBaseMarche(ABC):
    @abstractmethod
    def acheter_graines(self, graine: GrainesEnum) -> None: ...

    @abstractmethod
    def acheter_animal(self, animal_type: AnimauxEnum) -> None: ...

    @abstractmethod
    def vendre_produit(self) -> None: ...

