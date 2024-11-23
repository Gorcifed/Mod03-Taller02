from abc import ABC, abstractmethod
from models.ianimal import IAnimal

# Clase que representa un animal
class Animal(IAnimal):
    def __init__(self, nombre:str, edad: int, peso:float)-> None:
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.sonido = ""

    def serializar(self):
        return self.__dict__
    
    # Get nombre
    @property
    def nombre(self) -> str:
        return self.__nombre

    # Set nombre
    @nombre.setter
    def nombre(self, value:str) -> None:
        if(isinstance(value, str)):
            self.__nombre = value
        else:
            raise ValueError("Expected type str")

    # Get edad
    @property
    def edad(self) -> int:
        return self.__edad

    # Set edad
    @edad.setter
    def edad(self, value:int) -> None:
        if(isinstance(value, int)):
            self.__edad= value
        else:
            raise ValueError("Expected type int")

    # Get peso
    @property
    def peso(self) -> float:
        return self.__peso

    # Set peso
    @peso.setter
    def peso(self, value:float) -> None:
        if(isinstance(value, float)):
            self.__peso= value
        else:
            raise ValueError("Expected type float")

    @property
    def sonido(self) -> str:
        """ Devuelve el valor del atributo privado 'sonido' """
        return self.__sonido

    @sonido.setter
    def sonido(self, value:str) -> None:
        """
        Establece un nuevo valor para el atributo privado 'sonido'

        Valida que el valor enviado corresponda al tipo de dato del atributo
        """
        if isinstance(value, str):
            self.__sonido = value
        else:
            raise ValueError('Expected str')

    #Métodos
    @abstractmethod
    def hacer_sonido(self):
        pass

    def comer(self, kilos)-> None:
        self.kilos_comidos += kilos

    def obtener_kilos_comidos(self) -> float:
        return self.kilos_comidos