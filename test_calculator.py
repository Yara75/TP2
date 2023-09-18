import pytest
from calculator import calculator

def test_add():
    assert calculator.add(1,1) == 2
    assert calculator.add(-1,1) == 0

def test_add2():
    assert calculator.add(10,10) == 20







