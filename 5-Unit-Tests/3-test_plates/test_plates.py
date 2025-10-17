import pytest
from plates import is_valid


def main():
    test_length()
    test_firsttwo()
    test_spacepunctuation()
    test_num_notinmiddle()

def test_length():
    assert is_valid("HARITS") == True
    assert is_valid("H") == False

def test_firsttwo():
    assert is_valid("AB") == True
    assert is_valid("12") == False

def test_spacepunctuation():
    assert is_valid("KUU.24") == False
    assert is_valid("HELLO,HAR") == False

def test_num_notinmiddle():
    assert is_valid("KU24KU") == False
    assert is_valid("KUU24") == True
    assert is_valid("KU02") == False

if __name__ == "__main__":
    main()

