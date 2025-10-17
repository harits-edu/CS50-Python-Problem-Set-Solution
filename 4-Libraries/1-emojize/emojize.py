import emoji

def main():
    emojitext = input("Enter your emoji: ")
    print(f"Output:{emoji.emojize(emojitext, language= "alias")}")

main()
