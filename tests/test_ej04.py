import pytest
from src.ej04 import validarNumero, cuentaAtras

def test_validarNumero():
    assert validarNumero("12")

def test_cuentaAtras():
    assert cuentaAtras(5) == [5, 4, 3, 2, 1]