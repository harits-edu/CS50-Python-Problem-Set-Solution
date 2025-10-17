def main():

    var = input("Expressions: ")
    x, y, z = var.split(" ")
    x = float(x)
    z = float(z)
    print(interpret(x, y, z))

def interpret(a, b, c):
    if b == "+":
        return a + c
    elif b == "-":
        return a - c
    elif b == "*":
        return a * c
    elif b == "/":
        return a / c

main()
