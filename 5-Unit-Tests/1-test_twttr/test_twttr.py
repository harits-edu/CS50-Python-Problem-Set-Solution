import pytest
from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("harits") == "hrts"
    assert shorten("kuu24") == "k24"
    assert shorten("The Black Cat") == "Th Blck Ct"
    assert shorten("Harits Ganteng!!!!!") == "Hrts Gntng!!!!!"
    assert shorten("HARITS") == "HRTS"

if __name__ == "__main__":
    main()
