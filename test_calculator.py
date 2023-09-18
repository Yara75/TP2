import pytest
from calculator import Calculator


class TestCalculator:

    def __init__(self):
        self.cal = Calculator()

    def test_add(self):
        assert Calculator.add(self.cal, 1, 1) == 2
        assert Calculator.add(self.cal, -1, 1) == 0

    def test_add2(self):
        assert Calculator.add(self.cal, 10, 10) == 20

    def test_substract(self):
        assert Calculator.subtract(self.cal, 10, -1) == 9
        assert Calculator.subtract(self.cal, -10, -1) == -11
        assert Calculator.subtract(self.cal, 0, -0) == 0
        assert Calculator.subtract(self.cal, "ze", 1) == Exception
