import pytest
from jar import Jar


def test_init():

    # Initial Condition for test_init()
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # Another test
    jar2 = Jar(capacity = 10, size = 10)
    assert jar2.capacity == 10
    assert jar2.size == 10

    # Invalid capacity
    with pytest.raises(ValueError):
        Jar(capacity = -10, size = 10)


def test_str():

    # First it's empty
    jar = Jar()
    assert str(jar) == ""

    # Adding 1 cookie
    jar.deposit(1)
    assert str(jar) == "🍪"

    # Adding 3 more cookies, now there's 4
    jar.deposit(3)
    assert str(jar) == "🍪" * 4


def test_deposit():

    # Initially it was zero, then we use deposit
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

    jar.deposit(7)
    assert jar.size == 12

    # What if it exceeds to capacity?
    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():

    # Now testing withdraw
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(6)
    assert jar.size == 6

    jar.withdraw(6)
    assert jar.size == 0

    # What if there's no available cookies in the jar?
    with pytest.raises(ValueError):
        jar.withdraw(1)
