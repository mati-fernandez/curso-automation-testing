import pytest

from calculadora import sumar,restar,multiplicar,dividir

@pytest.fixture
def numeros_enteros():
    return 20, 5, 11

@pytest.fixture
def numeros_decimales():
    return 0.1, 0.2, 0.5

@pytest.mark.smoke
@pytest.mark.operador
@pytest.mark.parametrize(
    "a,b,esperado",
    [
        (1, 2, 3),
        (5, 5, 10),
        (-2, 3, 1)
    ]
)
def test_sumar(a, b, esperado):
    assert sumar(a, b) == esperado

@pytest.mark.parametrize(
    "a,b,esperado",
    [
        (10, 5, 5),
        (5, 10, -5),
        (0, 3, -3),
    ]
)
def test_restar(a, b, esperado):
    assert restar(a, b) == esperado

def test_multiplicar(numeros_decimales):
    a, b, c = numeros_decimales
    assert  multiplicar(a, b) == pytest.approx(0.02)
    assert  multiplicar(a, c) == pytest.approx(0.05)

def test_dividir(numeros_enteros):
    a, b, c = numeros_enteros
    assert dividir(a, b) == 4
    assert dividir(b, c) == pytest.approx(0.4545454545)

@pytest.mark.exception
def test_dividir_por_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(9,0)

