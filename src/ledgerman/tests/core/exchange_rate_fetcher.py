from unittest import TestCase

from ledgerman import *


class TestExchangeAPI(TestCase):

    """
    Tests related to the ExchangeRateFetcher / API Connectors.
    """

    def test_fetch_ecb(self):

        """
        ExchangeAPI: Test European Central Bank API (XML)
        """

        Money.fetchRates("ecb")
        Money("1 EUR").to("USD")

    def test_fetch_exchangeratesapi_io(self):

        """
        ExchangeAPI: Test exchangeratesapi.io API (JSON)
        """

        Money.fetchRates("exchangeratesapi_io")
        Money("1 EUR").to("USD")

    def test_fetch_bitpanda(self):

        """
        ExchangeAPI: Test Bitpanda Crypto API (JSON)
        """

        Money.fetchRates("bitpanda")
        Money("1 EUR").to("BEST")

    def test_fetch_coingecko(self):

        """
        ExchangeAPI: Test CoinGecko Crypto API (JSON)
        """

        Money.fetchRates("coingecko")
        Money("1 EUR").to("BTC")
