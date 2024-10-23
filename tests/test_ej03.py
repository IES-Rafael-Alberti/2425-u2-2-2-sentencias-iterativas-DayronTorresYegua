import pytest
from src.ej03 import validarNumero, listaImpares

def test_validarEdad():
    assert validarNumero("12")

def test_listaImpares():
    assert listaImpares(10) == [1, 3, 5, 7, 9]