import pytest
from src.ej02 import validarEdad

def test_validarEdad():
    assert validarEdad("12")
    assert validarEdad("we") is None
    assert validarEdad("-1") is None