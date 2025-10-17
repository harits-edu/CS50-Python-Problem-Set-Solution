import sys


class Jar:

    # The two main attributes of the class, capacity and size.
    # Both assignment (doesn't use underscore convention)
    # will reference to the setter definied later.
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    # Simple way to print multiple cookie emoji ^_^.
    def __str__(self):
        return "🍪" * self._size

    # A instance method to deal with the size attributes, will be used on main.
    def deposit(self, n):
        if self._size + n <= self._capacity:
            self._size += n
        else:
            raise ValueError("Exceeds maximum capacity")

    # A instance method to deal with the size attributes, will be used on main.
    def withdraw(self, n):
        if self._size - n >= 0:
            self._size -= n
        else:
            raise ValueError("There's not enough cookies")

    # Altho not explicitly used in main, this getter connects __innit__
    # to the setter so the validation would work (I think)
    @property
    def capacity(self):
        return self._capacity

    # Validation of values with setter
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity must be non-negative")
        self._capacity = capacity

    # This getter is explicitly used in main to call the size (number of cookies)
    @property
    def size(self):
        return self._size

    # Validation of values with setter
    @size.setter
    def size(self, size):
        if size < 0 or size > self._capacity:
            raise ValueError("Invalid size")
        self._size = size


def main():

    # Creates an Instance of Class Jar()
    cookieJar = Jar()

    while True:

        # The Main Menu
        print(
            """Press 1 to Deposit Cookies
Press 2 to Withdraw Cookies
Press 3 to Check the Number of Cookies
Press 4 to Exit Program\n"""
        )

        n = int(input("Enter your option: "))

        # I haven't put any error catching on case 1 or case 2
        match n:
            case 1:
                cookieJar.deposit(int(input("Total Cookies to Deposit: ")))
            case 2:
                cookieJar.withdraw(int(input("Total Cookies to Withdraw: ")))
            case 3:
                print(f"The number of cookies is {cookieJar.size}")
                print(cookieJar)
            case 4:
                sys.exit("Program Exited")
            case _:
                print("Invalid option")


if __name__ == "__main__":
    main()
