import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    octet = r"(1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])"
    pattern = r"^" + octet + r"\." + octet + r"\." + octet + r"\." + octet + r"$"
    if matches := re.search(pattern, ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
