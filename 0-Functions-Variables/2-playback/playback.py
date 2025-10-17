def main():
    text = input("Enter whatever text you want: ")
    playback_func(text)

def playback_func(txt):
    txt = txt.replace(" ","...", count=-1)
    print(txt)

main()
