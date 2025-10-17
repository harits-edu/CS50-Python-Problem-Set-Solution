# Import library, terutama sys
import sys

# Cek input argument sys di awal
# Jika sys arg terlalu sedikit, sys exit
# Jika sys arg terlalu banyak, sys exit
# Jika sys arg bukan file python, sys exit
# Jika file tidak ada, sys exit
# Jika sys arg sesuai, hitung jumlah lines


def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    name, ext = sys.argv[1].split(".")

    if ext != "py":
        print("Not a Python file")
        sys.exit(1)

    try:
        count = 0
        with open(sys.argv[1]) as file:
            for line in file:
                if (line.strip() == "") or (line.strip().startswith("#")):
                    count += 0
                else:
                    count += 1
            print(count)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)


if __name__ == "__main__":
    main()
