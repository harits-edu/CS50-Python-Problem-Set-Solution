def main():
    textInput = input("camelCase: ")
    print(camel(textInput))

def camel(txt):
    result = ""
    for ch in txt:
        if ch.isupper():
            result += "_" + ch.lower()
        else:
            result += ch.lower()
    return result

main()
