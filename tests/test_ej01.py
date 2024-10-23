import pytest
from src.ej01 import validarPalabra

def test_validarpalabra():
    assert validarPalabra("Hola123") is None
    assert validarPalabra("Hola") == "Hola"
    assert validarPalabra("") is None
    assert validarPalabra("~¬@") is None
