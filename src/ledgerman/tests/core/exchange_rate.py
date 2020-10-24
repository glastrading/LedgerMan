from unittest import TestCase

from ledgerman import *


class TestExchangeRate(TestCase):

    """
    Test ExchangeRates
    """

    def test_init(self):

        """
        Test Exchange Rate creation.
        """

        ExchangeRate("EUR", "USD", 1.2)

    def test_inverse(self):

        """
        Test inversing Exchange Rates.
        """

        e = ExchangeRate("EUR", "USD", 1.2)
        i = e.inverse()
        self.assertEquals(e, e.inverse())

    def test_convert(self):

        """
        Test money conversions.
        """

        e = ExchangeRate("A", "XYZ", 2)

        self.assertEquals(
            e.convert(Money("3 A")),
            Money("6 XYZ"),
            "Forward money conversions should work properly.",
        )
        self.assertEquals(
            e.convert(Money("3 XYZ")),
            Money("1.5 A"),
            "Backwards money conversions should work properly.",
        )

    def test_equals(self):

        """
        Test the equality function of Exchange Rates.
        """

        self.assertEquals(ExchangeRate("A", "B", 1), ExchangeRate("A", "B", 1))
        self.assertEquals(ExchangeRate("A", "C", 2), ExchangeRate("C", "A", 0.5))
        self.assertEquals(ExchangeRate("A", "C", 3), ExchangeRate("C", "A", 1 / 3))
        self.assertEquals(ExchangeRate("A", "C", 1.2), ExchangeRate("C", "A", 1 / 1.2))
        self.assertEquals(ExchangeRate("A", "C", 1), ExchangeRate("C", "A", 1))

    def test_hash(self):

        """
        Test the hashing function.
        """

        self.assertFalse(
            hash(ExchangeRate("A", "B", 2)) == hash(ExchangeRate("A", "B", 3)),
            "Different Rates should hash differently.",
        )
        self.assertEquals(
            hash(ExchangeRate("A", "B", 2)),
            hash(ExchangeRate("B", "A", 0.5)),
            "Inverse Rates should hash equally.",
        )
