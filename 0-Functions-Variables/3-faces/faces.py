def main():
    emoji = input("Enter the text with emoticon: ")
    convert(emoji)
    print("Thanks for entering your emoji and text!")

def convert(emo):
    emo = emo.replace(":)", "🙂").replace(":(", "🙁")
    print(emo)

main()
