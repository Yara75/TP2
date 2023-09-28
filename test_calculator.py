import pytest
from calculator import Calculator


class TestCalculator:

    def test_add(self):
        cal = Calculator()
        assert cal.add(1, 1) == 2
        assert cal.add(-1, 1) == 0

    def test_subtract(self):
        cal = Calculator()
        assert cal.subtract(10, -1) == 11
        assert cal.subtract(-10, -1) == -9
        assert cal.subtract(0, -0) == 0

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

    def test_divide(self):
        cal = Calculator()
        assert cal.divide(10, 5) == 2
        assert cal.divide(2, 2) == 1
        assert cal.divide(10, 20) == 0.5
        assert cal.divide(1, 3) == 0.3333333333333333

    def test_divide_exception(self):
        cal = Calculator()
        with pytest.raises(ZeroDivisionError):
            cal.divide(3, 0)

    def test_multiply(self):
        cal = Calculator()
        assert cal.multiply(2, 2) == 4
        assert cal.multiply(2, 0) == 0
        assert cal.multiply(2, -2) == -4
        assert cal.multiply(2, 0.5) == 1.0
        assert cal.multiply(2, -0.5) == -1.0
        assert cal.multiply(2, 0.0) == 0.0
        assert cal.multiply(2, -0.0) == -0.0
        assert cal.multiply(2, 0.0000000001) == 0.0000000002

    def test_multiply_exception(self):
        cal = Calculator()
        with pytest.raises(TypeError):
            cal.multiply("ze", 1)
