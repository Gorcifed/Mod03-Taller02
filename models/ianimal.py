from abc import ABC, abstractmethod

# Interface que representa a un animal que come
class IAnimal(ABC):
    @abstractmethod
    def comer(self, kilos) -> None:
        pass

    def obtener_kilos_comidos(self) -> float:
        pass