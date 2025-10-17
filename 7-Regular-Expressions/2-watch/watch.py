import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([A-Za-z0-9_-]{11})"'
    matches = re.search(pattern, s)
    if matches:
        return "https://youtu.be/" + matches.group(1)
    else:
        return None


if __name__ == "__main__":
    main()
