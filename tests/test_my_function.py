import pytest
import source.my_functions as mf
import time

def test_add():
    result = mf.add(number_one=1, number_two=5)
    assert result == 6

def test_divide():
    result_02 = mf.divide(number_one=1, number_two=5)
    assert result_02 == 0.2

def test_divide_zero():
    # with pytest.raises(ZeroDivisionError):
    #     mf.divide(number_one=42, number_two=0)
    with pytest.raises(ValueError):
        mf.divide(number_one=42, number_two=0)


def test_concate():
    result = mf.add(number_one="J'aime les ", number_two="tacos")
    assert result == "J'aime les tacos"

def test_multiply():
    result_positif = mf.multiply(number_one=2, number_two=21)
    assert result_positif == 42

    result_negative = mf.multiply(number_one=2, number_two=-21)
    assert result_negative == -42

    result_zero = mf.multiply(number_one=2, number_two=0)
    assert result_zero == 0


@pytest.mark.slooow
def test_multiply_slow():
    time.sleep(1)
    result = mf.multiply(number_one=3, number_two= 3)
    assert result == 9