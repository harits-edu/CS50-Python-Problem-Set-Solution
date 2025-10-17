from PIL import Image, ImageOps
import sys


def main():
    # Check for length of sys.argv
    if len(sys.argv) < 3:
        sys.exit("Too few command-line argument")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    infile = sys.argv[1]
    outfile = sys.argv[2]

    try:
        _, inExtension = infile.rsplit(".", 1)
        _, outExtension = outfile.rsplit(".", 1)
        extensionType = ["jpg", "jpeg", "png"]
    except ValueError:
        sys.exit("Invalid file name")

    if (inExtension.lower() not in extensionType) and (
        outExtension.lower() not in extensionType
    ):
        sys.exit("Invalid Output")

    if inExtension != outExtension:
        sys.exit("Input and output files have different extension")

    try:
        inputPic = Image.open(infile)
        shirtPic = Image.open("shirt.png")
        shirtSize = shirtPic.size
        fittedInput = ImageOps.fit(inputPic, shirtSize)
        fittedInput.paste(shirtPic, (0, 0), mask=shirtPic)
        fittedInput.save(outfile)
    except FileNotFoundError:
        sys.exit("Input picture does not exist")


if __name__ == "__main__":
    main()
