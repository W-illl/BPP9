import pytest
from funciones import suma,resta,dividir

def test_suma():
    assert suma(5,5) == 10
   
def test_resta():
    assert resta(10,5) == 5

def test_division():
    assert dividir(10,5) == 2

def test_suma_FAIL():
    assert suma(3,3) == 5

def test_division_FAIL():
    assert dividir(12,3) == 2

def test_resta_FAIL():
    assert resta(12,5) == 5