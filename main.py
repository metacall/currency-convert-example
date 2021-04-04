import json
from urllib.request import urlopen

with urlopen("http://api.exchangeratesapi.io/v1/latest?access_key=<YOUR_API_KEY>&format=1") as response:
    source = response.read()

data = json.loads(source)


# function for coversion
def convertCurrency(amount, _from, _to):

    rateArray = data["rates"]

    fromR = rateArray.get(_from)
    toR = rateArray.get(_to)

    total = amount * toR / fromR
    print(str(amount) + " " + _from + " = " + str(total) + " " + _to)


# convertCurrency(100, "USD", "INR")
