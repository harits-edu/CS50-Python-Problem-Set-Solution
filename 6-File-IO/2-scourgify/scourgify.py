# Import sys
# Import csv

import sys
import csv


def main():

    # Check for length of sys.argv
    if len(sys.argv) < 3:
        sys.exit("Too few command-line argument")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Read before.csv
    # Write after.csv
    infile = sys.argv[1]
    outfile = sys.argv[2]
    try:
        with open(infile, newline="") as f_in, open(outfile, "w", newline="") as f_out:
            reader = csv.DictReader(f_in)

            writer = csv.DictWriter(f_out, fieldnames=["first", "last", "house"])
            writer.writeheader()

            for row in reader:
                last, first = row["name"].split(",")
                house = row["house"]
                writer.writerow(
                    {"first": first.strip(), "last": last.strip(), "house": house}
                )

    except FileNotFoundError:
        # Check if csv file exists
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()
