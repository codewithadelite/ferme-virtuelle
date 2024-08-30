class Culture:
    def __init__(self, type_de_culture: str, temp_de_croissance: int):
        self.__type_de_culture = type_de_culture
        self.__temp_croissance = temp_de_croissance
        self.__revenu: int = 0

    @property
    def type_de_culture(self) -> str:
        return self.__type_de_culture

    @property
    def temp_croissance(self) -> int:
        return self.__temp_croissance

    @property
    def revenu(self) -> int:
        return self.__revenu

