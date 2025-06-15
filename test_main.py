# test_main.py
import pytest
from main import greet


def test_greet():
    assert greet() == "Hello, CI"