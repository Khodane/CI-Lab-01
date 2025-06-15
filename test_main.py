# test_main.py
import pytest
from main import greet


def test_greet():
    assert greet() == "Goodbye, CI" # This will fail because greet() returns "Hello, CI"
