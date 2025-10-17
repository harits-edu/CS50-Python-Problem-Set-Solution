def main():
    mass_input = int(input("Enter how much mass it is! (in kg): "))
    einstein(mass_input)

def einstein(mass):
    energy = mass * 300000000**2
    print("Energy equals to ", energy)

main()
