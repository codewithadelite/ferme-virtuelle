from .ferme import Ferme
from ..interfaces.marche import AbastractBaseMarche


class Marche(AbastractBaseMarche):
    def __init__(self, ferme: Ferme):
        pass

    def acheter_graines(self):
        pass

    def acheter_animal(self):
        pass

    def vendre_produit(self):
        pass



