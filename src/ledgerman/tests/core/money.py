from unittest import TestCase

from ledgerman import *


class TestMoney(TestCase):

    """
    Money Tests.
    """

    def test_money_init(self):

        """
        Test Money Initialisation.
        """

        Money()

        Money("5 EUR")
        Money("20 USD")

        Money("1.5 BTC")
        Money("-200 EUR")
        Money("-200.0778 EUR")

        Money("1.5 EUR", roundTo="0.1")

    def test_money_repr(self):

        """
        Test Money Representation.
        """

        print(Money())
        print(Money("1.8 BTC"))
        print(Money("1.888876502928 BTC", roundTo="0.1"))

    def test_money_to(self):

        """
        Test simple Money conversions.
        """

        Money().to("EUR")
        Money("1.8 BTC").to("BTC")

        try:
            Money("1.8 XXXXXXX").to("TTTT")
            raise Exception("Conversion should have failed.")
        except ValueError:
            pass

    def test_money_equality(self):

        """
        Test Money equality functions.
        """

        self.assertEquals(Money(), Money())
        self.assertEquals(Money(), Money("0 EUR"))
        self.assertEquals(Money("100 EUR"), Money("100 EUR"))

        self.assertTrue(Money() == Money("0 EUR"))
        self.assertFalse(Money() != Money("0 EUR"))

        self.assertTrue(Money() != Money("12 EUR"))
        self.assertFalse(Money() == Money("12 EUR"))

        self.assertEquals(Money("1.0 EUR"), Money("1 EUR"))
        self.assertFalse(Money("1.000000000000000000001 EUR") == Money("1 EUR"))

    def test_money_add(self):

        """
        Test Money addition.
        """

        self.assertEquals(Money("100 EUR"), Money("50 EUR") + Money("50 EUR"))
        self.assertEquals(Money("1 EUR"), Money("0 EUR") + Money("1 EUR"))
        self.assertEquals(Money("1.50 EUR"), Money("1.23 EUR") + Money(".27 EUR"))
        self.assertEquals(Money("1.00 EUR"), Money("1.23 EUR") + Money("-.23 EUR"))

    def test_money_sub(self):

        """
        Test Money subtraction.
        """

        self.assertEquals(Money("0 EUR"), Money("50 EUR") - Money("50 EUR"))
        self.assertEquals(Money("-1 EUR"), Money("0 EUR") - Money("1 EUR"))
        self.assertEquals(Money("1.50 EUR"), Money("2.00 EUR") - Money(".50 EUR"))

    def test_money_neg(self):

        """
        Test Money negation.
        """

        self.assertEquals(Money("0 EUR") - Money("2 EUR"), -Money("2 EUR"))
        self.assertEquals(Money("0 EUR") - Money("-2 EUR"), -Money("-2 EUR"))

    def test_money_mul(self):

        """
        Test Money multiplication.
        """

        try:
            Money("0 EUR") * Money("2 EUR")
            raise Exception("Should not be able to multiply Money and Money.")
        except TypeError:
            pass

        self.assertEquals(Money("0 EUR") * 100, Money("0 EUR"))
        self.assertEquals(Money("1 EUR") * 5, Money("5 EUR"))
        self.assertEquals(Money("1 EUR") * 5.33, Money("5.33 EUR"))
        self.assertEquals(Money("1 EUR") * 5.3344, Money("5.3344 EUR"))
        self.assertEquals(Money("2 EUR") * -5, Money("-10 EUR"))

    def test_money_div(self):

        """
        Test Money division.
        """

        self.assertEquals(Money("2 EUR") / Money("2 EUR"), 1)
        self.assertEquals(Money("4 EUR") / Money("2 EUR"), 2)
        self.assertEquals(Money("3 EUR") / Money("2 EUR"), 3 / 2)

        self.assertEquals(Money("3 EUR") / 2, Money("1.5 EUR"))
        self.assertEquals(Money("100 EUR") / 3, Money("200 EUR") / 6)
