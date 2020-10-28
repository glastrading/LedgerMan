from unittest import TestCase

from ledgerman import *


class TestExchange(TestCase):

    """
    Test Exchanges.
    """

    def test_init(self):

        """
        Exchange: Test initialization
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
        Exchange: Test money conversions
        """

        e = Exchange(
            ("A", "B", 1.4),
            ("B", "C", 3),
            ("C", "D", 420),
            ("D", "E", 3),
            ("E", "F", 5),
        )

        self.assertTrue(
            abs((e.convert(Money("1 A"), "B") - Money("1.4 B")).amount) < 0.01,
            "First-level Money conversions should work properly.",
        )

        self.assertTrue(
            abs((e.convert(Money("1 A"), "C") - Money("4.2 C")).amount) < 0.01,
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
        Exchange: Test equality function
        """

        self.assertEquals(Exchange(["A", "B", 1]), Exchange(["A", "B", 1]))

    def test_serialization(self):

        """
        Exchange: Test serialization
        """

        e1 = Exchange(["A", "B", 3.2])
        e2 = Exchange.deserialize(e1.serialize())

        self.assertEquals(e1, e2)
