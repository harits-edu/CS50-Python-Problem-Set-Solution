from validator_collection import validators, checkers, errors


def main():
    email = input("What's your email address? ")
    print("Valid") if check(email) == True else print("Invalid")


def check(s):
    is_email_address = checkers.is_email(s)
    return is_email_address


main()
