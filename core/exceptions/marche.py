class InvalidGraineSpaceError(Exception):
    def __init__(self, message: str = "Il n'y a pas assez d'espace de culture"):
        super().__init__(message)


class NoEnoughMoneyError(Exception):
    def __init__(self, message: str = "Pas assez d'argent"):
        super().__init__(message)

