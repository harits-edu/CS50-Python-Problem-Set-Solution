import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^([0-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM) to ([0-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM)$"
    matches = re.search(pattern, s)

    if not matches:
        raise ValueError

    startHour, startMin, startM = matches.group(1), matches.group(2), matches.group(3)
    endHour, endMin, endM = matches.group(4), matches.group(5), matches.group(6)

    startHour = int(startHour)
    endHour = int(endHour)

    startMin = startMin if startMin else "00"
    endMin = endMin if endMin else "00"

    startHour = convert_hour(startHour, startM)
    endHour = convert_hour(endHour, endM)

    return f"{startHour:02}:{startMin} to {endHour:02}:{endMin}"


def convert_hour(hour, meridiem):
    if meridiem == "AM":
        return 0 if hour == 12 else hour
    else:  # PM
        return 12 if hour == 12 else hour + 12


if __name__ == "__main__":
    main()
