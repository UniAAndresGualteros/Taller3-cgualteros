import unittest
from models.boa_constrictor import Boa_Constrictor

class TestBoa(unittest.TestCase):
    
    def test_hacer_sonido(self):
        boa1 = Boa_Constrictor("Rosita", 12.8, 4, "Colombia", 0.0)
        self.assertEqual(boa1.hacer_sonido(),"¡Tsss!") 
        
    def test_calcular_flete(self):
        boa1 = Boa_Constrictor("Rosita", 12.8, 4, "Colombia", 0.0)
        self.assertEqual(boa1.calcular_flete(),0)
        
    def test_agregar_ratones(self):
        boa1 = Boa_Constrictor("Rosita", 12.8, 4, "Colombia", 0.0)
        boa1.agregar_ratones()
        self.assertEqual(boa1.obtener_ratones(),1)
        
        
        
if __name__ == '__main__':
    unittest.main()
         