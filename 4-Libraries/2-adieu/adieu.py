import sys

nameList = []


def main():
    while True:
        try:
            inputName = input("Name: ")
            nameList.append(inputName)
        except EOFError:
            print()
            print("Adieu, adieu, to", end=" ")
            for name in nameList:
                if len(nameList) == 1:
                    print(name)
                elif nameList.index(name) == (len(nameList) - 1):
                    print(f"and {name}")
                elif len(nameList) == 2:
                    print(f"{name}", end=" ")
                else:
                    print(f"{name},", end=" ")
            sys.exit(0)


main()
