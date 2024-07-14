import unittest
from models.huron import Huron

class TestHuron(unittest.TestCase):
    
    def test_hacer_sonido(self):
        huron1 = Huron("Felpita", 2.1, 1, "España", 150.4)
        self.assertEqual(huron1.hacer_sonido(),"¡Eek Eek!") 
         
    def test_calcular_flete(self):
        huron1 = Huron("Felpita", 2.1, 1, "España", 150.4)
        self.assertEqual(huron1.calcular_flete(),315.84)
        
if __name__ == '__main__':
    unittest.main()
        