def main():
    vartime = input("What time is it? ")
    total_hours = convert(vartime)

    if 7 <= total_hours <= 8:
        print("breakfast time")
    elif 12 <= total_hours <= 13:
        print("lunch time")
    elif 18 <= total_hours <= 19:
        print("dinner time")

def convert(num):
    a, b = num.split(":")
    a = float(a)
    b = float(b)
    return a + (b / 60)

if __name__ == "__main__":
    main()
