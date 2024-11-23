from abc import ABC
from models.animal import Animal

# Clase que representa un perro
class Perro(Animal):
    #Constructor
    def __init__(self, nombre: str, edad: int, peso: float) -> None:
        super().__init__(nombre, edad, peso)

    #Métodos
    def hacer_sonido(self):
        return "¡Guau guau!"
    
    def serializar(self):
        return self.__dict__