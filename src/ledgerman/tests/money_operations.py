from unittest import TestCase

from ledgerman import *


class TestMoneyOperations(TestCase):
    """
    Tests related to the Money class and Money operations.
    """

    def test_init_empty(self):
        """
        Test Money().
        """
        m = Money()
        self.assertEqual(m.amount, 0, "Money amounts should be 0 at empty init.")
        self.assertEqual(m.currency, "EUR", "The default currency should be EUR")

    def test_init_number(self):
        """
        Test Money(amount).
        """
        m = Money(10)
        self.assertEqual(m.amount, 10, "Money amount should be (n) at init(n).")
        self.assertEqual(m.currency, "EUR", "The default currency should be EUR")

    def test_init_full(self):
        """
        Test Account(amount, currency).
        """
        m = Money(200, "ETH")
        self.assertEqual(m.amount, 200, "Money amount should be (n) at init(n, c).")
        self.assertEqual(
            m.currency, "ETH", "Money's currency should be (c) at init(n, c)."
        )

    def test_op_add(self):
        """
        Test Money + x.
        """
        m = Money(60) + Money(10)
        self.assertEqual(m.amount, 70, "Money should add with money properly.")
        m = Money() + 100
        self.assertEqual(m.amount, 100, "Money should add with integers properly.")
        m = Money() + 0.5
        self.assertEqual(m.amount, 0.5, "Money should add with floats properly.")

    def test_op_sub(self):
        """
        Test Money - x.
        """
        m = Money(100) - Money(60)
        self.assertEqual(m.amount, 40, "Money should subtract with money properly.")
        m = Money(50) - 50
        self.assertEqual(m.amount, 0, "Money should subtract with integers properly.")
        m = Money(0.5) - 0.5
        self.assertEqual(m.amount, 0, "Money should subtract with floats properly.")

    def test_op_negate(self):
        """
        Test -Money.
        """
        m = -Money(100)
        self.assertEqual(m.amount, -100, "Negating Money should negate ist amount.")

    def test_op_mul(self):
        """
        Test Money * x.
        """
        m = Money(50) * 2
        self.assertEqual(m.amount, 100, "Money should multiply with integers properly.")
        m = Money(50) * 0.5
        self.assertEqual(m.amount, 25, "Money should multiply with floats properly.")

    def test_op_div(self):
        """
        Test Money / x.
        """
        m = Money(100) / Money(25)
        self.assertEqual(m, 4, "Money should divide with money properly to an int.")
        m = Money(50) / 2
        self.assertEqual(m.amount, 25, "Money should divide with integers properly.")
        m = Money(25) / 0.5
        self.assertEqual(m.amount, 50, "Money should divide with floats properly.")
