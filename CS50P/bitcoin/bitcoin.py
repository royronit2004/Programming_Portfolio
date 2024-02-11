#bitcoin

import sys
import requests

if len(sys.argv) == 2:
    try:
        val = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)

else:
    print("Missing command-line argument")
    sys.exit(1)


try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = r.json()
    bitc = response["bpi"]["USD"]["rate_float"]
    total_amt = bitc * val
    print(f"${total_amt:,.4f}")

except requests.RequestException:
    print("RequestException")
    sys.exit(1)
