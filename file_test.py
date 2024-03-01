import pytest

def test_calc_addition():
    # Vérifie le résultat de l'addition 2+4
    output = 2 + 4
    assert output == 6

def test_calc_substraction():
    # Vérifie le résultat de la soustraction 2-4
    output = 2 - 4
    assert output == -2

def test_calc_multiply():
    # Vérifie le résultat de la multiplication 2*4
    output = 2 * 4
    assert output == 8

def test_coucou():
    # Vérifie que la chaîne de caractères renvoyée est 'hello'
    output = 'hello'
    assert output == 'hello'
    