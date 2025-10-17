def main():
    text = input("Input: ")
    short_text = shorten(text)
    print(short_text)


def shorten(word):
    result = ""
    for ch in word:
        if ch in ("a", "i", "u", "e", "o", "A", "I", "U", "E", "O"):
            result += ""
        else:
            result += ch
    return result


if __name__ == "__main__":
    main()
