from unittest import TestCase

from ledgerman import *


class TestExchangeAPI(TestCase):

    """
    Tests related to the ExchangeRateFetcher / API Connectors.
    """

    def test_fetch_ecb(self):

        """
        Test the European Central Banks XML API.
        """

        Money.fetchRates("ecb")
        Money("1 EUR").to("USD")

    def test_fetch_exchangeratesapi_io(self):

        """
        Test the exchangeratesapi.io JSON API.
        """

        Money.fetchRates("exchangeratesapi_io")
        Money("1 EUR").to("USD")

    def test_fetch_coingecko(self):

        """
        Test the CoinGecko Crypto JSON API.
        """

        Money.fetchRates("coingecko")
        Money("1 EUR").to("BTC")
