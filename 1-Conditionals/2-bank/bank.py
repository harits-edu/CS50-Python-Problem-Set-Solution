def main():
    greeting_var = input("Greeting: ")
    greeting_var = greeting_var.strip().lower()
    bank(greeting_var)

def bank(var):
    if "hello" in var:
        print("$0")
    elif var[0] == "h":
        print("$20")
    else:
        print("$100")

main()
