months = [
        "January","February","March","April",
        "May","June","July","August",
        "September","October","November","December"
        ]

def main():
    while True:
        date = input("Date: ").strip()
        try:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

        except ValueError:
            if "," not in date:
                continue
            try:
                month_tmp, rest = date.split(" ", 1)
                day, year = rest.replace(",", "").split()
                month = months.index(month_tmp.capitalize()) + 1
                day = int(day)
                year = int(year)
            except Exception:
                continue

        if (1 <= month <= 12) and (1 <= day <= 31):
            print(f"{year}-{month:02}-{day:02}")
            break
main()
