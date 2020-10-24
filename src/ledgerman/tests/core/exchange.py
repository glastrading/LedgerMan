from unittest import TestCase

from ledgerman import *


class TestExchange(TestCase):

    """
    Test Exchanges.
    """

    def test_init(self):

        """
        Test Exchange creation.
        """

        Exchange()
        Exchange(
            ("A", "B", 1.4),
            ("B", "C", 3),
            ("C", "D", 420),
            ("D", "E", 3),
            ("E", "F", 5),
        )

    def test_convert(self):

        """
        Test money conversions.
        """

        e = Exchange(
            ("A", "B", 1.4),
            ("B", "C", 3),
            ("C", "D", 420),
            ("D", "E", 3),
            ("E", "F", 5),
        )

        self.assertEquals(
            e.convert(Money("1 A"), "B"),
            Money("1.4 B"),
            "First-level Money conversions should work properly.",
        )

        self.assertEquals(
            e.convert(Money("1 A"), "C"),
            Money("4.2 C"),
            "Second-level Money conversions should work properly.",
        )

        self.assertEquals(
            e.convert(Money("1 A"), "D"),
            Money("1764 D"),
            "Third-level Money conversions should work properly.",
        )

        self.assertEquals(
            e.convert(Money("1 A"), "E"),
            Money("5292 E"),
            "Fourth-level Money conversions should work properly.",
        )

        self.assertEquals(
            e.convert(Money("1 A"), "F"),
            Money("26460 F"),
            "Fifth-level Money conversions should work properly.",
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
