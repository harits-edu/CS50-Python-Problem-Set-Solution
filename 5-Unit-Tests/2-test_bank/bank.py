def main():
    greeting_var = input("Greeting: ")
    greeting_var = greeting_var.strip().lower()
    n = value(greeting_var)
    print(f"${n}")

def value(greeting):
    if "hello" in greeting:
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
