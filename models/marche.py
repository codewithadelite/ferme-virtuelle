import random
from .ferme import Ferme
from core.interfaces.marche import AbastractBaseMarche
from core.exceptions.marche import InvalidGraineSpaceError, NoEnoughMoneyError
from core.types import Resorurce as ResourceType

from models.culture import Culture
from models.animal import Animal


class Marche(AbastractBaseMarche):
    def __init__(self, ferme: Ferme):
        self.ferme: Ferme = ferme

    def _ajouter_resource_a_la_ferme(self, resource: Culture | Animal):
        if isinstance(resource, Culture):
            self.ferme.cultures.append(resource)
            return
        if isinstance(resource, Animal):
            self.ferme.animaux.append(resource)
            return

    def acheter_graines(self, graines: ResourceType) -> None:
        """
        Achetez  graines et ajoutez-la à la ferme

        :param graines: (str)
        :return: (None)
        :raise: (InvalidGraineSpaceError)
        """
        if len(self.ferme.cultures) == self.ferme.espace:
            raise InvalidGraineSpaceError

        if self.ferme.argent < graines.prix:
            raise NoEnoughMoneyError

        temp_de_croissance = random.randint(1, 5)  # Temp de croissance généré de manière aléatoire.
        graine_obj: Culture = Culture(graines.nom, temp_de_croissance)

        self.ferme.argent -= graines.prix
        self._ajouter_resource_a_la_ferme(graine_obj)

    def acheter_animal(self, animal_type: ResourceType):
        """
        Achetez  animal et ajoutez-la à la ferme
        :param animal_type: (str)
        :return: (None)
        """
        if self.ferme.argent < animal_type.prix:
            raise NoEnoughMoneyError

        # le temps nécessaire pour atteindre l'âge adulte, généré de manière aléatoire.
        temp_adult = random.randint(1, 3)
        animal_obj: Animal = Animal(animal_type.nom, temp_adult)

        self.ferme.argent -= animal_type.prix
        self._ajouter_resource_a_la_ferme(animal_obj)

    def vendre_produit(self):
        pass



