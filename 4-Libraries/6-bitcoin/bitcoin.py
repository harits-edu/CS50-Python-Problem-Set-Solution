import requests
import sys
import json


def main():
    try:
        if len(sys.argv) != 2:
            print("Missing command-line argument")
            sys.exit(1)
        else:
            sys.argv[1] = float(sys.argv[1])
    except ValueError:
        print("Commnad-line argument is'nt a number")
        sys.exit(1)

    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=829776e79be8910404985c2ba39b7318500effc9ef4e551d034f3a0a47b9903d"
    )
    jsonResponse = response.json()
    # print(json.dumps(response.json(), indent=2))
    rate = float(jsonResponse["data"]["priceUsd"])
    totalRate = rate * sys.argv[1]
    print( f"${totalRate:,.4f}")


main()
