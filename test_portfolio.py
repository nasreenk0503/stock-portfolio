# test_portfolio.py
from portfolio import Portfolio
"""
p = Portfolio()
print(f"Empty portfolio cost: {p.cost()}")
p.buy("IBM", 100, 176.48)
print(f"With 100 IBM @ 176.48: {p.cost()}")
p.buy("HPQ", 100, 36.15)
print(f"With 100 HPQ @ 36.15: {p.cost()}")


p = Portfolio()
print(f"Empty portfolio cost: {p.cost()}, should be 0.0")
p.buy("IBM", 100, 176.48)
print(f"With 100 IBM @ 176.48: {p.cost()}, should be 17648.0")
p.buy("HPQ", 100, 36.15)
print(f"With 100 HPQ @ 36.15: {p.cost()}, should be 21263.0")


# problem here: don't know what is wrong with my answer, and if the first one is wrong, the other will fail as well
p = Portfolio()
print(f"Empty portfolio cost: {p.cost()}, should be 0.0")
assert p.cost() == 0.0
p.buy("IBM", 100, 176.48)
print(f"With 100 IBM @ 176.48: {p.cost()}, should be 17648.0")
assert p.cost() == 17648.0
p.buy("HPQ", 100, 36.15)
print(f"With 100 HPQ @ 36.15: {p.cost()}, should be 21263.0")
assert p.cost() == 21263.0
"""


# run pytest, python will find anything start with 'test', and test any file that starts wuth'test_' and consistant with the following name
import pytest
from portfolio import Portfolio

def test_empty_portfolio():
    p = Portfolio()
    assert p.cost() == 0.0

def test_buy_one_stock():
    p = Portfolio()
    p.buy("IBM", 100, 176.48)
    assert p.cost() == 17648.0

def test_buy_two_stock():
    p = Portfolio()
    p.buy("IBM", 100, 176.48)
    p.buy("HPQ", 100, 36.15)
    assert p.cost() == 21263.0

def test_not_enough_arguments_to_buy():
    p = Portfolio()
    with pytest.raises(TypeError): # if TypeError' raise, the block pass
        p.buy('IBM')
    """
    try:
        p.buy('IBM')
    except TypeError:
        pass
    else:
        assert False,'we did not have an error'
    """
