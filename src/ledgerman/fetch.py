import requests
from xml.etree import ElementTree as XMLElementTree


class ExchangeRateFetcher:
    """
    An API connector for ledgerman that fetches ExchangeRates.
    """

    @staticmethod
    def printExchangeRate(e):
        print(e[0], "=>", e[2], e[1])

    @staticmethod
    def fetch(source="ecb", verbose=False):
        """
        Fetch ExchangeRates from a source.
        """
        source = source.lower()
        exchangeRates = []
        # fetch, convert and return
        if source == "ecb":
            exchangeRates = ExchangeRateFetcher.fetch_ecb(verbose)
        elif source == "exchangeratesapi_io":
            exchangeRates = ExchangeRateFetcher.fetch_exchangeratesapi_io(verbose)
        else:
            raise ValueError("ExchangeRateFetcher: Invalid Source: " + source)
        return exchangeRates

    # APIs to fetch from
    @staticmethod
    def fetch_ecb(verbose=False):  # official, XML
        """
        Fetch ExchangeRates from the european central bank (updated daily).
        """
        exchangeRates = []
        # fetch
        r = requests.get(
            "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"
        )
        if r.status_code != 200:
            print("Connecting to the ECB XML API failed.")
            exit()
        # parse xml
        tree = XMLElementTree.fromstring(r.text)
        date = tree[2][0].attrib["time"]
        ratesData = tree[2][0]
        # convert data to ExchangeRates
        if verbose:
            print("ExchangeRates (ECB, " + date + "):")
        for d in ratesData:
            e = "EUR", d.attrib["currency"], float(d.attrib["rate"])
            if verbose:
                ExchangeRateFetcher.printExchangeRate(e)
            exchangeRates += [e]
        return exchangeRates

    @staticmethod
    def fetch_exchangeratesapi_io(verbose=False):  # inofficial, JSON
        """
        Fetch ExchangeRates from api.exchangeratesapi.io. Takes input
        """
        exchangeRates = []
        # fetch
        r = requests.get("https://api.exchangeratesapi.io/latest")
        if r.status_code != 200:
            print("Connecting to the exchangeratesapi.io JSON API failed.")
            return
        # parse json
        jsonResult = r.json()
        rates = jsonResult["rates"]
        base = jsonResult["base"]
        date = jsonResult["date"]
        # convert data to ExchangeRates
        if verbose:
            print("ExchangeRates (exchangeratesapi.io, " + date + "):")
        for currency in rates.keys():
            e = base, currency, rates[currency]
            if verbose:
                ExchangeRateFetcher.printExchangeRate(e)
            exchangeRates += [e]
        return exchangeRates
