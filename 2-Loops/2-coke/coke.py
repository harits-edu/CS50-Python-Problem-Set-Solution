def main():
    price = 50
    while price > 0:
        while True:
            coin = int(input("Insert Coin: "))
            if coin in [25, 10, 5]:
                break
            else:
                print("Amount Due:", price)
                continue

        price -= coin
        if price > 0:
            print("Amount Due:", price)
        elif price == 0:
            print("Change Owed:", price)
        else:
            print("Change Owed:", price * -1)

main()
