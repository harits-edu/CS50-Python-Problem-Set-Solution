from pyfiglet import Figlet
import sys
import random


def main():
    figlet = Figlet()
    fontList = figlet.getFonts()

    if len(sys.argv) not in (1, 3):
        sys.exit(1)

    if len(sys.argv) == 1:
        fontname = random.choice(fontList)
        figlet.setFont(font=fontname)

    elif len(sys.argv) == 3:
        if (sys.argv[1] == "-f") or (sys.argv[1] == "--font"):

            if sys.argv[2] in fontList:
                fontname = sys.argv[2]

                figlet.setFont(font=fontname)

            else:
                print("Font isn't found")
                sys.exit(1)

        else:
            print("Input Arguments Invalid")
            sys.exit(1)

    text = input("Input your text: ")
    print(figlet.renderText(text))


main()
