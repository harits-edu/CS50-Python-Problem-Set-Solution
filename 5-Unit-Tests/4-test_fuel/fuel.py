def main():
    fraction = input("Fraction: ")
    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except (ValueError, ZeroDivisionError):
        pass


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
    except ValueError:
        raise ValueError("X and Y must be integers")

    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    if x > y or x < 0 or y < 0:
        raise ValueError("Invalid fraction")

    percentage = round((x / y) * 100)
    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
