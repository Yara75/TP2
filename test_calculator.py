import pytest
import math
from calculator import Calculator


class TestCalculator:

    def test_add(self):
        cal = Calculator()
        assert cal.add(1, 1) == 2
        assert cal.add(-1, 1) == 0
        assert cal.add(-5, -20) == -25
        result = cal.add(-2.4, 7.8)
        assert round(result, 1) == 5.4
        assert round(cal.add(math.sqrt(4), 7.8), 1) == 9.8
        assert round(cal.add(math.sqrt(7), math.sqrt(26)), 2) == 7.74
        assert round(cal.add(-15, math.sqrt(11.3)), 3) == -11.638
        assert cal.add("TP2", " DevOps") == "TP2 DevOps"
        assert cal.add(True, True) == 2
        assert cal.add(False, True) == 1
        assert cal.add(False, False) == 0
        assert cal.add([1, 2], [3, 4]) == [1, 2, 3, 4]
        assert cal.add(["DevOps", None], ["Machine learning", "Réseaux"]) == ["DevOps", None, "Machine learning", "Réseaux"]

    def test_subtract(self):
        cal = Calculator()
        assert cal.subtract(10, -1) == 11
        assert cal.subtract(-10, -1) == -9
        assert cal.subtract(0, -0) == 0
        assert round(cal.subtract(-15, 45.84), 2) == -60.84
        assert round(cal.subtract(8, -(math.sqrt(3))), 3) == 9.732
        assert cal.subtract(False, True) == -1
        assert cal.subtract(True, True) == 0
        assert cal.subtract(3j, round(math.pi, 1)) == 3j - 3.1


    def test_subtract_float(self):
        cal = Calculator()
        result = cal.subtract(10.3, 5.3)
        assert abs(result - 5.0) < 1e-6  # Rounding precision
        result = cal.subtract(3.7, 5.9)
        assert abs(result + 2.2) < 1e-6
        result = cal.subtract(10.1, 10.1)
        assert result < 1e-6

    def test_subtract_exception(self):
        cal = Calculator()
        with pytest.raises(TypeError):
            cal.subtract("ze", 1)
            cal.subtract(None, 1)
            cal.subtract([1, 2, 3], 8)
            cal.subtract("DevOps", True)

    def test_divide(self):
        cal = Calculator()
        assert cal.divide(10, 5) == 2
        assert cal.divide(2, -2) == -1
        assert cal.divide(10, 20) == 0.5
        assert cal.divide(1, 3) == 0.3333333333333333
        assert round(cal.divide(-18.8, 87), 4) == -0.2161
        assert cal.divide(0, 3) == None
        assert round(cal.divide(math.sqrt(4), math.sqrt(12)), 1) == 0.6


    def test_divide_exception(self):
        cal = Calculator()
        with pytest.raises(ZeroDivisionError):
            cal.divide(3, 0)

    def test_multiply(self):
        cal = Calculator()
        assert cal.multiply(6, 5) == 30
        assert cal.multiply(2, 0) == 0
        assert cal.multiply(9, -3) == -27
        assert cal.multiply(True, False) == 0
        assert cal.multiply(True, True) == 1
        assert cal.multiply(2, 0.5) == 1.0
        assert cal.multiply(-0.5, 2) == -1.0
        assert cal.multiply(4, 3) == 12
        assert cal.multiply(2, 0.0) == 0.0
        assert cal.multiply(2, -0.0) == -0.0
        assert cal.multiply(2j + 4, 5j + 1) == -6+22j
        assert cal.multiply(2, 0.0000000001) == 0.0000000002

    def test_exposant(self):
        cal = Calculator()
        assert cal.exposant(2, 3) == 8
        assert cal.exposant(115, 0) == 1
  
    def test_pourcent(self):
        cal = Calculator()
        assert cal.pourcent(20, 140) == 28
        assert cal.pourcent(50, 70) == 35

    def test_average(self):
        cal = Calculator()
        assert cal.average(17, 15) == 16
        assert cal.average(13, 8) == 10.5
