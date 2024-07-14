#from models.animal_exotico import Animal_Exotico
from animal_exotico import Animal_Exotico

class Huron(Animal_Exotico):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        
        
    def hacer_sonido(self):
        return "¡Eek Eek!"
    
    def dar_informacion(self):
        return f"{self._nombre} - {self._peso}kg, {self._edad}años, Pais Origen:{self._pais_origen}, Impuestos:{self._impuestos}"
    
    def __repr__(self):
        return self.dar_informacion()
    
    
