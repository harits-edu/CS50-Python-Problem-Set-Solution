import pytest
from fuel import convert, gauge

def main():
    test_convert()
    test_gauge()
    test_error()

def test_convert():
    assert convert("2/3") == 67
    assert convert("2/2") == 100
    assert convert("1/100") == 1

def test_gauge():
    assert gauge(67) == "67%"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_error():
    with pytest.raises(ValueError):
        convert("cat/rat")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("-1/2")



if __name__ == "__main__":
    main()

