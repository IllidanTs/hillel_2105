import pytest
import test_functions_new

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (10, 5, 15),
    (-1, -1, -2),
    (0, 0, 0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 1, 1),
    (10, 5, 5),
    (-1, -1, 0),
    (0, 0, 0)
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (10, 5, 50),
    (-1, -1, 1),
    (0, 10, 0)
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (9, 3, 3),
    pytest.param(1, 0, "Cannot divide by zero", marks=pytest.mark.xfail),
    pytest.param(0, 0, "Cannot divide by zero", marks=pytest.mark.xfail)
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected

@pytest.mark.parametrize("num, expected", [
    (2, True),
    (3, False),
    (0, True),
    (-2, True),
    (-3, False)
])
def test_is_even(num, expected):
    assert is_even(num) == expected

@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 1),
    (5, 120),
    pytest.param(-1, "Invalid input", marks=pytest.mark.skip(reason="Negative input not supported")),
    (3, 6)
])
def test_factorial(n, expected):
    assert test_functions_new.factorial(n) == expected
