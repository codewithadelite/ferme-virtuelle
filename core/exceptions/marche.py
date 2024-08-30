class InvalidGraineSpaceError(Exception):
    def __init__(self, message: str = "Il n'y a pas assez d'espace de culture"):
        super().__init__(message)
