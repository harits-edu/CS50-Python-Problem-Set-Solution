import pytest
from seasons import convertMinutesToWords

def main():
    test_convert()

def test_convert():

    # This code is written in 2025-10-07, change the argument with one year before your current time
    # Altho 2024 is a leap year, It starts way after February 29th
    assert convertMinutesToWords("2024-10-07") == "Five hundred twenty-five thousand, six hundred minutes"

    # Two years before, 2024 is a leap year
    assert convertMinutesToWords("2023-10-07") == "One million, fifty-two thousand, six hundred forty minutes"

def test_invalid_date():

    # Did sys.exit(1) activates when the date is invalid?
    with pytest.raises(SystemExit):
        convertMinutesToWords("Invalid Date")


if __name__ == "__main__":
    main()
