from datetime import date
import inflect
import sys


def main():

    # Getting user's input and prints result returned by the function
    birthday = input("Date of Birth: ")
    print(convertMinutesToWords(birthday))


def convertMinutesToWords(birthday):

    # Getting today's time, "now" now references to a date object of the time right now.
    now = date.today()

    # Error checking, If the time is invalid, the program exits.
    try:
        birthdayObject = date.fromisoformat(birthday)
    except ValueError:
        sys.exit("Invalid Time")

    # Idk how this works, but apparantly (overlap) subtracting two dates returns a timedelta object
    delta = now - birthdayObject
    minutes = int(delta.total_seconds() / 60)

    # Using inflect library to convert number to words directly, a cool library ngl.
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="").capitalize()

    return f"{words} minutes"


if __name__ == "__main__":
    main()
