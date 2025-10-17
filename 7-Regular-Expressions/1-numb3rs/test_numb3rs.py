import pytest
from numb3rs import validate

def main():
    test_validate()

def test_shorten():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("192.168.001.1") == False
    assert validate("cat") == False

if __name__ == "__main__":
    main()
