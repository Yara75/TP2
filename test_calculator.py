import pytest
from calculator import Calculator

def test_add():
    assert Calculator.add(1,1) == 2
    assert Calculator.add(-1,1) == 0

def test_add2():
    assert Calculator.add(10,10) == 20







