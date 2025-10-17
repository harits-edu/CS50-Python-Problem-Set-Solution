def main():
    var = input("Plate: ")
    if is_valid(var):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    checks = ""

    if 2 <= len(plate) <= 6:
        checks += "1"

    foundDigit = False

    for i in range(len(plate)):
        if plate[i].isdigit():
            foundDigit = True
            letter = plate[0:i]
            num = plate[i:]

            if len(letter) >= 2:
                checks += "1"

            if letter.isalpha():
                checks += "1"

            if num.isdigit() and num[0] != "0":
                checks += "1"

            break

    if not foundDigit and (2 <= len(plate) <= 6) and plate.isalpha():
        checks += "111"

    if checks == "1111":
        return True
    else:
        return False


main()
