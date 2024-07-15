#from models.animal_exotico import Animal_Exotico
from animal_exotico import Animal_Exotico

class Boa_Constrictor(Animal_Exotico):
    
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self.__ratones = 0
        
    def hacer_sonido(self):
        return "¡Tsss!"
    
    def agregar_ratones(self):
        if self.__ratones >=20:
            raise ValueError("Demasiados Ratones!")
        else:
            self.__ratones += 1
        
        
    def obtener_ratones(self):   
        return self.__ratones
    
    def dar_informacion(self):
        return f"{self._nombre} - {self._peso}kg, {self._edad}años, Pais Origen:{self._pais_origen}, Impuestos:{self._impuestos}"
    
    def __repr__(self):
        return self.dar_informacion()
            
