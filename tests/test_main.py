import pytest
from app.main import run_vending_machine

def test_exact_payment():
    assert run_vending_machine([25, 25]) == 0

def test_overpayment():
    assert run_vending_machine([25, 25, 10]) == 10

def test_multiple_small_coins():
    assert run_vending_machine([10, 10, 5, 5, 5]) == 0

def test_invalid_coin():
    assert run_vending_machine([3, 1, 7, 25, 25]) == 0

def test_no_input_returns():
    assert run_vending_machine([]) == 50

