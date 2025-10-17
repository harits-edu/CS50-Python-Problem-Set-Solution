def main():
    question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    deep(question)

def deep(answer):
    answer = answer.strip().lower()
    match answer:
        case "42" | "fourty-two" | "forty two" | "forty-two":
            print("Yes")
        case _:
            print("No")

main()
