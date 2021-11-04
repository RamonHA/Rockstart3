import pytest
from poo import *

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
    pass