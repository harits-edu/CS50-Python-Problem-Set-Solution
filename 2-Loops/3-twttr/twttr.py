def main():
    text = input("Input: ")
    removevowels(text)

def removevowels(txt):
    result = ""
    for ch in txt:
        if ch in ("a", "i", "u", "e", "o", "A", "I", "U", "E", "O"):
            result += ""
        else:
            result += ch
    print("Output:", result)

main()

