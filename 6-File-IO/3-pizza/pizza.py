# Import Tabulate
# Import sys, csv

from tabulate import tabulate
import sys
import csv

# Check for sys.argv length
# Check for extension
# Check if file exists
# Read and tabulate csv

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        table = []
        with open(filename) as file:
            reader = csv.DictReader(file)
            for row in reader:
                table.append(row)
            print(tabulate(table, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
