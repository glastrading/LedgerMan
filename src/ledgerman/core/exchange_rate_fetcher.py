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
        elif source == "coingecko":
            exchangeRates = ExchangeRateFetcher.fetch_coingecko(verbose)
        else:
            raise ValueError("ExchangeRateFetcher: Invalid Source: " + source)
        return exchangeRates

    # APIs to fetch from
    @staticmethod
    def fetch_ecb(verbose=False):  # REAL: official, XML, Free

        """
        Fetch ExchangeRates from the european central bank (updated daily).
        """

        exchangeRates = []
        # fetch
        r = requests.get(
            "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"
        )
        if r.status_code != 200:
            raise IOError("Connecting to the ECB XML API failed.")
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
    def fetch_exchangeratesapi_io(verbose=False):  # REAL: inofficial, JSON, Free

        """
        Fetch ExchangeRates from api.exchangeratesapi.io (which takes input from ecb).
        """

        exchangeRates = []
        # fetch
        r = requests.get("https://api.exchangeratesapi.io/latest")
        if r.status_code != 200:
            raise IOError("Connecting to the exchangeratesapi.io JSON API failed.")
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

    @staticmethod
    def fetch_coingecko(verbose=False):  # CRYPTO: inofficial, JSON, Free

        """
        Fetch ExchangeRates from api.coingecko.com.
        Docs: https://www.coingecko.com/api/documentations/v3
        """

        exchangeRates = []

        coingecko_sym2id = {  # see https://api.coingecko.com/api/v3/coins/list
            "eth": "ethereum",
            "btc": "bitcoin",
            "ltc": "litecoin",
            "trx": "tron",
            "usdt": "tether",
            "xrp": "ripple",
            "link": "chainlink",
            "best": "bitpanda-ecosystem-token",
            "pan": "pantos",
            "miota": "iota",
            "ada": "cardano",
            "vet": "vechain",
            "omg": "omisego",
            "neo": "neo",
            "qtum": "qtum",
            "xem": "nem",
            "xtz": "tezos",
            "yfi": "yearn-finance",
            "chz": "chiliz",
            "xlm": "stellar",
            "ont": "ontology",
            "bch": "bitcoin-cash",
            "usdc": "usd-coin",
            "eos": "eos",
            "uni": "uniswap",
            "waves": "waves",
            "atom": "cosmos",
            "dot": "polkadot",
            "snx": "havven",
            "dash": "dash",
            "zrx": "0x",
            "bat": "basic-attention-token",
            "kmd": "komodo",
            "etc": "ethereum-classic",
            "doge": "dogecoin",
            "zec": "zcash",
            "rep": "augur",
            "lsk": "lisk",
            "comp": "compound-governance-token",
            "mkr": "maker",
        }
        coingecko_id2sym = {v: k for k, v in coingecko_sym2id.items()}
        # build query
        request_url = "https://api.coingecko.com/api/v3/simple/price?ids="
        request_url += ",".join(coingecko_sym2id.values())
        request_url += "&vs_currencies=eur"
        # fetch
        r = requests.get(request_url)
        if r.status_code != 200:
            raise IOError("Connecting to the coingecko.com JSON API failed.")
        # parse json
        jsonResult = r.json()

        # convert data to ExchangeRates
        if verbose:
            print("ExchangeRates (coingecko.com):")
        for id in jsonResult.keys():
            rates = jsonResult[id]
            e = coingecko_id2sym[id].upper(), "EUR", rates["eur"]
            if verbose:
                ExchangeRateFetcher.printExchangeRate(e)
            exchangeRates += [e]
        return exchangeRates
