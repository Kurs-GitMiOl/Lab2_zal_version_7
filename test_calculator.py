import math
from calculator import Calculator


# Tests addition
def test_sum_positive_numbers():
    calc_1 = Calculator(10.0, 5.0)
    assert math.isclose(calc_1.sum(), 15.0, rel_tol=1e-9)


def test_sum_negative_numbers():
    calc_1 = Calculator(-10.0, -5.0)
    assert math.isclose(calc_1.sum(), -15.0, rel_tol=1e-9)


def test_sum_mixed_sign_numbers():
    calc_1 = Calculator(-10.0, 5.0)
    assert math.isclose(calc_1.sum(), -5.0, rel_tol=1e-9)


def test_sum_with_zero():
    calc_1 = Calculator(10.0, 0.0)
    assert math.isclose(calc_1.sum(), 10.0, rel_tol=1e-9)


# Tests subtraction
def test_subtract_positive_numbers():
    calc_1 = Calculator(10.0, 5.0)
    assert math.isclose(calc_1.subtract(), 5.0, rel_tol=1e-9)


def test_subtract_negative_numbers():
    calc_1 = Calculator(-5.5, -1.0)
    assert math.isclose(calc_1.subtract(), -4.5, rel_tol=1e-9)


def test_subtract_mixed_sign_numbers():
    calc_1 = Calculator(-5.5, 1.0)
    assert math.isclose(calc_1.subtract(), -6.5, rel_tol=1e-9)


def test_subtract_with_zero():
    calc_1 = Calculator(7.0, 0.0)
    assert math.isclose(calc_1.subtract(), 7.0, rel_tol=1e-9)


# Tests multiplication
def test_multiply_positive_numbers():
    calc_1 = Calculator(10.0, 5.0)
    assert math.isclose(calc_1.multiply(), 50.0, rel_tol=1e-9)


def test_multiply_negative_numbers():
    calc_1 = Calculator(-10.0, -5.0)
    assert math.isclose(calc_1.multiply(), 50.0, rel_tol=1e-9)


def test_multiply_mixed_sign_numbers():
    calc_1 = Calculator(-10.0, 5.0)
    assert math.isclose(calc_1.multiply(), -50.0, rel_tol=1e-9)


def test_multiply_with_zero():
    calc_1 = Calculator(0.0, 5.0)
    assert math.isclose(calc_1.multiply(), 0.0, rel_tol=1e-9)


# Tests division with correct numbers
def test_division_positive_numbers():
    calc_1 = Calculator(10.0, 5.0)
    assert math.isclose(calc_1.divide(), 2.0, rel_tol=1e-9)


def test_division_negative_numbers():
    calc_1 = Calculator(-10.0, -5.0)
    assert math.isclose(calc_1.divide(), 2.0, rel_tol=1e-9)


def test_division_mixed_sign_numbers():
    calc_1 = Calculator(-10.0, 5.0)
    assert math.isclose(calc_1.divide(), -2.0, rel_tol=1e-9)


# Test division  with op2 == 0.0
def test_divide_by_zero():
    calc_1 = Calculator(10.0, 0.0)
    assert calc_1.divide() == "Error - division by zero!!!"




