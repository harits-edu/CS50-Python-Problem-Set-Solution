import random


def main():
    while True:
        try:
            n = int(input("Level: "))
            break
        except ValueError:
            pass

    randomNumber = random.randint(1, n)

    while True:
        while True:
            try:
                guessNumber = int(input("Guess: "))
                break
            except ValueError:
                continue

        if guessNumber > 0:
            if guessNumber == randomNumber:
                print("Just right!")
                break
            elif guessNumber >= randomNumber:
                print("Too large!")
            elif guessNumber <= randomNumber:
                print("Too small!")
        else:
            continue


main()
