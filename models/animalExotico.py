from abc import ABC
from models.animal import Animal

# Clase que representa un animal exótico
class AnimalExotico(Animal):
    def __init__(self, nombre: str, edad: int, peso:float, pais_origen: str, impuestos: float) -> None:
        self.pais_origen = pais_origen
        self.impuestos = impuestos
        super().__init__(nombre, edad, peso)

    @property
    def pais_origen(self) -> str:
        """ Devuelve el valor del atributo privado 'pais_origen' """
        return self.__pais_origen

    @pais_origen.setter
    def pais_origen(self, value:str) -> None:
        """
        Establece un nuevo valor para el atributo privado 'pais_origen'

        Valida que el valor enviado corresponda al tipo de dato del atributo
        """
        if isinstance(value, str):
            self.__pais_origen = value
        else:
            raise ValueError('Expected str')

    @property
    def impuestos(self) -> float:
            """ Devuelve el valor del atributo privado 'impuesto' """
            return self._impuesto

    @impuestos.setter
    def impuestos(self, value:float) -> None:
        """
        Establece un nuevo valor para el atributo privado 'impuesto'
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """
        if isinstance(value, float):
            self._impuesto = value
        else:
            raise ValueError('Expected float')

    def hacer_sonido(self):
        pass