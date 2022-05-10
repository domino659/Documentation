# pytest pytest_test.py -v
# pytest pytest_test.py -v --html=index.html

import pytest

from main import add, divide

def test_add_two_numbers():
    assert add(5, 10) == 15

def test_add_two_letters():
    assert add("a", "b") == "ab"

def test_add_two_booleans():
    assert add(True, False) == 1
    assert add(True, True) == 2
    assert add(False, False) == 0

def test_add_two_none():
    # Vérifie que none ne marche pas 
    with pytest.raises(TypeError):
        add(None, None)

def test_divide_two_numbers():
    assert divide(10, 2) == 5
