from boaConstrictor import BoaConstrictor
from huron import Huron

class Guarderia():
    _boa1 = BoaConstrictor("Margarita", 5, 2.0,"Colombia",20.2)
    _boa2 = BoaConstrictor("Tata", 3, 2.1,"Brasil",220.2)
    _uron1 = Huron("Pepe", 5, 2.5, "Guatemala", 52.23)
    _uron2 = Huron("Lolo", 2, 1.5, "Costa rica", 74.13)

    def alimentar_boa(self, boa):
        try:
            if(boa == None or (boa != self._boa1 and boa != self._boa2)):
                raise ValueError("Esta Boa no existe!")

            boa.comer_raton()
            print("Éxito")
        except ValueError as e:
            print (e)
