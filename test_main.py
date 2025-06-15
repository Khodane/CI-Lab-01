# test_main.py
<<<<<<< HEAD
from main import greet

def test_greet():
    assert greet() == "Hello, CI!"
=======
import pytest
from main import greet


def test_greet():
    assert greet() == "Goodbye, CI" # This will fail because greet() returns "Hello, CI"
>>>>>>> 2d6bad44963750494c954dbcb0ba84a350996793
