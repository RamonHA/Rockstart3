import pytest
from src.poo import Pantalla

def test_one():
    assert True

def test_two():
    raise Exception

@pytest.mark.parametrize(
    "arg1",
    [
        "ana",
        "appa",
        "mama"
    ]
)
def test_palindromo(arg1):
    assert arg1 == arg1[::-1]

def test_pantalla():
    tv_samsung = Pantalla(999.99, 3000, 500, 1980)
    assert tv_samsung.get_voltaje() == 500