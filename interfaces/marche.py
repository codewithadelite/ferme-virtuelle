from abc import ABC, abstractmethod


class AbastractBaseMarche(ABC):
    @abstractmethod
    def acheter_graines(self): ...

    @abstractmethod
    def acheter_animal(self): ...

    @abstractmethod
    def vendre_produit(self): ...

