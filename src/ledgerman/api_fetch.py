import requests

from .money import Money


def fetch_exchangeratesapi():
    """
    Fetch all available ExchangeRates from exchangeratesapi.io.
    As they are from the european central bank, there's no crypto.
    """

    r = requests.get("https://api.exchangeratesapi.io/latest")

    if r.status_code != 200:
        print("Fetching from exchangeratesapi.io failed.")
        return

    jsonResult = r.json()
    rates = jsonResult["rates"]
    base = jsonResult["base"]
    date = jsonResult["date"]

    for currency in rates.keys():
        Money.addExchangeRate(base, currency, rates[currency])
