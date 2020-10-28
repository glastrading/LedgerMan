from unittest import TestCase

from ledgerman import *


class TestAccount(TestCase):

    """
    Test Accounts.
    """

    def test_init(self):

        """
        Account: Test initialization
        """

        debit = Account("debit")
        credit = Account("credit")

    def test_credit_debit(self):

        """
        Account: Test credit() and debit()
        """

        cash = Account("asset")
        loan = Account("liability")
        amount = Money("10000 EUR")

        cash.debit(amount, loan)
        self.assertEquals(
            cash.balance,
            amount,
            "Debiting to a debit account should increase the account.",
        )
        self.assertEquals(
            loan.balance,
            amount,
            "Debiting to a debit account should increase the account credited from.",
        )

        loan.debit(amount, cash)

        self.assertEquals(
            loan.balance,
            Money("0 EUR"),
            "Loan should be 0 after it is payed off.",
        )

    def test_increase_decrease(self):

        """
        Account: Test increasing and decreasing
        """

        cash = Account("asset")
        loan = Account("liability")
        amount = Money("10000 EUR")

        cash.increase(amount, loan)
        self.assertEquals(
            cash.balance,
            amount,
            "Increase on a debit account should debit to it.",
        )
        self.assertEquals(
            loan.balance,
            amount,
            "Increase on a debit account should credit the account decreased by it.",
        )

        loan.decrease(amount, cash)

        self.assertEquals(
            loan.balance,
            Money("0 EUR"),
            "Loan should be 0 after it is payed off.",
        )

    def test_transaction_notes(self):

        """
        Account: Test naming and annotating transactions
        """

        cash = Account("debit", name="My Wallet")
        loan = Account("credit", name="My Loan")

        amount = Money("10000 EUR")
        cash.debit(amount, loan, note="Take the loan from my bank.")
        loan.debit(amount, cash, note="Pay back what I owe the bank.")

    def test_serialization(self):

        """
        Account: Test serialization
        """

        a1 = Account("debit")
        a2 = Account.deserialize(a1.serialize())

        self.assertEquals(a1, a2)

        a3 = Account("debit")
        a3.debit("20 EUR", a1)
        a4 = Account.deserialize(a3.serialize())

        self.assertEquals(a3, a4)
