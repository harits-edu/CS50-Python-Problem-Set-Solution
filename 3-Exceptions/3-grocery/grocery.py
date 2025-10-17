def main():
    grocery = {}

    while True:
        try:
            item = input()
            item = item.upper()

            if item in grocery:
                grocery[item] += 1

            else:
                grocery[item] = 1
        except KeyError:
            pass

        except EOFError:
            for stuff, count in sorted(grocery.items()):
                print(f"{count} {stuff}")
            break

main()
