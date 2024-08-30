from abc import ABC, abstractmethod
from ..types import Resorurce as ResourceType


class AbastractBaseMarche(ABC):
    @abstractmethod
    def acheter_graines(self, graine: ResourceType) -> None: ...

    @abstractmethod
    def acheter_animal(self, animal_type: ResourceType) -> None: ...

    @abstractmethod
    def vendre_produit(self) -> None: ...

