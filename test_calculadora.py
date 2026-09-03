import pytest

from calculadora import sumar,restar,multiplicar,dividir

@pytest.mark.operador
def test_sumar():
    resultado = sumar(5,3)
    assert resultado == 8

def test_restar():
    resultado = restar(10,4)
    assert resultado == 6

def test_multiplicar():
    resultado = multiplicar(5,3)
    assert resultado == 15

def test_dividir():
    resultado = dividir(10,2)
    assert resultado == 5

def test_dividir_por_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(9,0)

