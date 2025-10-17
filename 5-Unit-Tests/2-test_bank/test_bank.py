import pytest
from bank import value

def main():
    test_zero()
    test_twenty()
    test_hundred()

def test_zero():
    assert value("Hello, Harits") == 0
    assert value("hello, Harits") == 0
    assert value("Hellooo, Harits") == 0

def test_twenty():
    assert value("Hi, Harits") == 20
    assert value("How you doing?, Harits") == 20
    assert value("Hey, Harits") == 20

def test_hundred():
    assert value("Got u, Harits") == 100
    assert value("What's up?, Harits") == 100
    assert value("Sup, Harits") == 100

if __name__ == "__main__":
    main()
