from ianimal import iAnimal
from animal import Animal
from animal_exotico import Animal_Exotico
from boa_constrictor import Boa_Constrictor
from huron import Huron


huron1 = Huron("Felpita", 2.1, 1, "España", 150.4)
boa1 = Boa_Constrictor("Rosita", 12.8, 4, "Colombia", 0.0)

print(huron1.obtener_nombre()+" - Sonido: "+huron1.hacer_sonido())
print(boa1.obtener_nombre()+" - Sonido: "+boa1.hacer_sonido())

print("Es huron")
print(isinstance(huron1, Huron))
print("Es Animal exotico")
print(isinstance(huron1, Animal_Exotico))
print("Es Animal")
print(isinstance(huron1, Animal))
print("Es iAnimal")
print(isinstance(huron1, iAnimal))
print("\n \n")
print("Es Boa")
print(isinstance(boa1, Boa_Constrictor))
print("Es Animal exotico")
print(isinstance(boa1, Animal_Exotico))
print("Es Animal")
print(isinstance(boa1, Animal))
print("Es iAnimal")
print(isinstance(boa1, iAnimal))

