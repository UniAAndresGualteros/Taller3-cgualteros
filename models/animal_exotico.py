#from models.animal import Animal
from animal import Animal

class Animal_Exotico(Animal):
    
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, peso, edad)
        self._pais_origen = pais_origen
        self._impuestos = impuestos
        
    def calcular_flete(self):
        calculo_flete = round(self.__impuestos * self._peso,2)
        return calculo_flete
    
    def dar_pais_origen(self):
        return self._pais_origen
    
    def dar_impuestos(self):
        return self._impuestos
    
    