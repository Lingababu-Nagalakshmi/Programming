import math
import pytest

def test_square():
    num= 25
    assert math.sqrt(num) == 5
test_square()

def testsquare():
    num = 7
    assert 7*7 == 49
testsquare()

def testequality():
    assert  10 == 10
testequality()

def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case('python') == 'Python'


# test_calculator.py



'''Pytest Inbuilt methods
1)xfail
2)skip
3)parametrize
4)Customised Markers'''

