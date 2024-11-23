from abc import ABC
from models.animalExotico import AnimalExotico

# Clase que representa un Hurón
class Huron(AnimalExotico):
    #Constructor
    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, edad, peso, pais_origen, impuestos)

    #Métodos
    def hacer_sonido(self):
        return "¡Eek Eek!"