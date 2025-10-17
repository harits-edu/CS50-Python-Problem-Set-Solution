def main():
    percentage = getp()

    if percentage >= 99:
        print("F")
    elif percentage <= 1:
        print("E")
    else:
        print(f'{percentage}%')

def getp():
    while True:
        try:
            while True:
                fraction = input("Fraction: ")
                n, d = fraction.split('/')
                n = round(float(n), 2)
                d = round(float(d), 2)
                if n.is_integer() and d.is_integer():
                    break

            p = round((n/d) * 100)
            if p < 0 or p > 100:
                raise ValueError
            return p
        except (ValueError, ZeroDivisionError):
            pass
main()
