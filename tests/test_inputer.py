import pytest
from unittest.mock import patch
from src.data_inputer import Inputer

def test_get_user_input_valid():
    """Checks if method converts to int"""
    inputer = Inputer()
    
    with patch("builtins.input", return_value="42"):
        result = inputer.get_user_input("Podaj liczbę: ")
    
    assert result == 42
    assert inputer.k == 42 

def test_get_user_input_float():
    """Check if accepts flow and converts to int"""
    inputer = Inputer()
    
    with patch("builtins.input", return_value="10.0"):
        result = inputer.get_user_input("Podaj liczbę: ")
    
    assert result == 10
    assert inputer.k == 10

def test_get_user_input_invalid(monkeypatch):
    """Check if the method catches wrong input"""
    inputer = Inputer()
    
    inputs = iter(["abc", "-5", "3.5", "7"])  # simulation wrong inputs
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    result = inputer.get_user_input("Podaj liczbę: ")
    
    assert result == 7
    assert inputer.k == 7
