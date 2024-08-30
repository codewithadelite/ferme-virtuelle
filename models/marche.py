import random
from .ferme import Ferme
from core.interfaces.marche import AbastractBaseMarche
from core.enumerations import AnimauxEnum, GrainesEnum
from core.exceptions.marche import InvalidGraineSpaceError

from models.culture import Culture
from models.animal import Animal


class Marche(AbastractBaseMarche):
    def __init__(self, ferme: Ferme):
        self.ferme: Ferme = ferme

    def acheter_graines(self, graines: str) -> None:
        """
        Achetez  graines et ajoutez-la à la ferme

        :param graines: (str)
        :return: (None)
        :raise: (InvalidGraineSpaceError)
        """
        if len(self.ferme.cultures) == self.ferme.espace:
            raise InvalidGraineSpaceError

        temp_de_croissance = random.randint(1, 5)  # Temp de croissance généré de manière aléatoire.
        graine_obj: Culture = Culture(graines, temp_de_croissance)

        self.ferme.cultures.append(graine_obj)

    def acheter_animal(self, animal_type: str):
        # le temps nécessaire pour atteindre l'âge adulte, généré de manière aléatoire.
        temp_adult = random.randint(1, 3)
        animal_obj: Animal = Animal(animal_type, temp_adult)
        self.ferme.animaux.append(animal_obj)

    def vendre_produit(self):
        pass



