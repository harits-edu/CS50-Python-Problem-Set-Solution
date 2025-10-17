import random


def main():
    levelx = get_level()

    score = 0

    for i in range(10):
        x = generate_integer(levelx)
        y = generate_integer(levelx)
        result = x + y
        count = 3

        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                count -= 1
                if count == 0:
                    print(f"{x} + {y} = {result}")
                    break
            if answer == result:
                score += 1
                break
            else:
                print("EEE")
                count -= 1
                if count == 0:
                    print(f"{x} + {y} = {result}")
                    break

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
