from unittest import TestCase

from ledgerman import *


class TestExchanges(TestCase):
    """
    Tests related to the ExchangeRate and the Exchange class.
    """

    # exchangeRate
    def test_rate_init(self):
        """
        Test ExchangeRate(a, b, n).
        """
        e = ExchangeRate("A", "B", 2)
        self.assertEqual(
            e.getCurrencies(),
            {"A", "B"},
            "ExchangeRates currencies should be {a,b} on init(a, b, n)",
        )
        self.assertEqual(e.rate, 2, "ExchangeRates rate should be (n) on init(a, b, n)")

    def test_rate_invert(self):
        """
        Test ExchangeRate.invert().
        """
        e = ExchangeRate("A", "B", 5)
        e_inv = e.inverse()
        self.assertEqual(
            e_inv.rate, 1 / e.rate, "Inverted ExchangeRates should invert the rate."
        )
        self.assertEqual(
            e_inv.base,
            e.other,
            "Inverted ExchangeRates should have the other currencies as their base.",
        )
        self.assertEqual(
            e_inv.other,
            e.base,
            "Inverted ExchangeRates should have the other currencies as their base.",
        )

    def test_rate_convert(self):
        """
        Test ExchangeRate.convert(money).
        """
        e = ExchangeRate("A", "B", 2)
        # A -> B
        m = e.convert(Money(2, "A"))
        self.assertEqual(
            m.amount,
            4,
            "ExchangeRates(A, B, r) should convert A to B properly by amount.",
        )
        self.assertEqual(
            m.currency,
            "B",
            "ExchangeRates(A, B, r) should convert A to money with currency B.",
        )
        # B -> A
        m = e.convert(Money(10, "B"))
        self.assertEqual(
            m.amount,
            5,
            "ExchangeRates(A, B, r) should convert B to A properly by amount.",
        )
        self.assertEqual(
            m.currency,
            "A",
            "ExchangeRates(A, B, r) should convert B to money with currency A.",
        )

    # exchange
    def test_exchange_init_empty(self):
        """
        Test Exchange().
        """
        e = Exchange()
        self.assertEqual(len(e), 0, "Exchanges should be empty on empty init.")

    def test_exchange_init_rates(self):
        """
        Test Exchange(*exchangeRates).
        """
        # rates init
        e = Exchange(ExchangeRate("A", "B", 2), ExchangeRate("B", "C", 3))
        self.assertEqual(len(e), 2, "Exchanges should have len 2 on init(e1, e2).")
        # lists / tuples init
        e = Exchange(["A", "B", 2], ["B", "C", 3])
        self.assertEqual(len(e), 2, "Exchanges should have len 2 on init(e1, e2).")

    def test_exchange_convert(self):
        """
        Test Exchange.convert(money, currency).
        """
        e = Exchange(["A", "B", 2], ["B", "C", 3])
        # A -> B
        m = e.convert(Money(2, "A"), "B")
        self.assertEqual(
            m.amount,
            4,
            "Exchanges with A -> 2 B should convert A to B properly by amount.",
        )
        self.assertEqual(
            m.currency,
            "B",
            "Exchanges with A -> 2 B should convert A to money with currency B.",
        )
        # B -> A
        m = e.convert(Money(10, "B"), "A")
        self.assertEqual(
            m.amount,
            5,
            "Exchanges with A -> 2 B should convert B to A properly by amount.",
        )
        self.assertEqual(
            m.currency,
            "A",
            "Exchanges with A -> 2 B should convert B to money with currency A.",
        )
