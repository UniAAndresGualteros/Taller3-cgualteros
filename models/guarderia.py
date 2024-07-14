from huron import Huron
from boa_constrictor import Boa_Constrictor

class Guarderia():
    
    def __init__(self) -> None:
        self.__nombre = "La Favorita"
        self.__direccion = "CL Falsa 123"
        self.__animales = []
        
    def agregar_animal(self, nuevo_animal):
        self.__animales.append(nuevo_animal)
        
         
    def dar_informacion(self):
        return f"Guarderia: {self.__nombre} Ubicacion: {self.__direccion} - Animales: {self.__animales}"
    
    def retornar_animales(self):
        return self.__animales
    
   
    def alimentar_boa(self,nombre_boa:str):
        for animal in self.__animales:
            if animal.obtener_nombre() == nombre_boa:
                try:
                    animal.agregar_ratones()
                    return "Éxito"
                except ValueError as e:
                    return f"La boa está llena: {e}"
        return f"Esta Boa no existe!"
    
    
        
    
boa1 = Boa_Constrictor("Rosita", 12.8, 4, "Colombia", 0.0)
boa2 = Boa_Constrictor("Devorador", 24.3, 1, "Francia", 258.9)
huron1 = Huron("Felpita", 2.1, 1, "España", 150.4)
huron2 = Huron("Lupita", 1.8, 2, "USA", 224.7)

guarderia1 = Guarderia()

guarderia1.agregar_animal(boa1)
guarderia1.agregar_animal(boa2)
guarderia1.agregar_animal(huron1)
guarderia1.agregar_animal(huron2)


print(guarderia1.dar_informacion())
print(boa1.obtener_nombre())

new_nombre_boa = "Rosita"

print(guarderia1.alimentar_boa(new_nombre_boa))
print(guarderia1.alimentar_boa(new_nombre_boa))
print(guarderia1.alimentar_boa(new_nombre_boa))
print(guarderia1.alimentar_boa(new_nombre_boa))
print(guarderia1.alimentar_boa(new_nombre_boa))
print(guarderia1.alimentar_boa(new_nombre_boa))
print(guarderia1.alimentar_boa(new_nombre_boa))
print(guarderia1.alimentar_boa(new_nombre_boa))
print(guarderia1.alimentar_boa(new_nombre_boa))
print(guarderia1.alimentar_boa(new_nombre_boa))
print(guarderia1.alimentar_boa(new_nombre_boa))

new_nombre_boa = "Rosito"

print(guarderia1.alimentar_boa(new_nombre_boa)) 
