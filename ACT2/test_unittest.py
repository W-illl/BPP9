import unittest
from funciones import suma,resta,dividir

class Test_funciones(unittest.TestCase):
    def test_suma(self):
        resultado = suma(5,5)
        self.assertEqual(resultado,10)
    
    def test_resta(self):
        resultado = resta(10,5)
        self.assertEqual(resultado,5)
    
    def test_division(self):
        resultado = dividir(10,5)
        self.assertEqual(resultado,2)
    
    def test_suma_FAIL(self):
        resultado = suma(3,3)
        self.assertEqual(resultado,5)
    
    def test_division_FAIL(self):
        resultado = dividir(12,3)
        self.assertEqual(resultado,2)

    def test_resta_FAIL(self):
        resultado = resta(12,5)
        self.assertEqual(resultado,5)
    