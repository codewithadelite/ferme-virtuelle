class Animal:
    def __init__(self, animal_type: str, temp_adulte: int):
        self.__animal_type = animal_type
        self.__temp_adulte = temp_adulte
        self.__revenu = 0

    @property
    def animal_type(self) -> str:
        return self.__animal_type

    @property
    def temp_adulte(self) -> int:
        return self.__temp_adulte

    @property
    def revenu(self) -> int:
        return self.__revenu



