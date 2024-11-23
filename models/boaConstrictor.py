from abc import ABC
from models.animalExotico import AnimalExotico

# Clase que representa una boa constrictor
class BoaConstrictor(AnimalExotico):
    #Constructor
    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str, impuestos: float, ratones_comidos: int = 0) -> None:
        self.ratones_comidos = ratones_comidos
        super().__init__(nombre, edad, peso, pais_origen, impuestos)

    @property
    def ratones_comidos(self) -> int:
        """ Devuelve el valor del atributo privado 'ratones_comidos' """
        return self.__ratones_comidos

    @ratones_comidos.setter
    def ratones_comidos(self, value:int) -> None:
        """
        Establece un nuevo valor para el atributo privado 'ratones_comidos'

        Valida que el valor enviado corresponda al tipo de dato del atributo
        """
        if isinstance(value, int):
            if(value < 0):
                raise ValueError('Expected positive int')
            self.__ratones_comidos = value
        else:
            raise ValueError('Expected int')

    #Métodos
    def hacer_sonido(self):
        return "¡Tsss!"
    
    def comer_raton(self):
        if(self.ratones_comidos == 10):
            raise ValueError("Demasiados Ratones")
        self.ratones_comidos += 1