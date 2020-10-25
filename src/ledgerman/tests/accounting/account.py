from unittest import TestCase

from ledgerman import *


class TestAccount(TestCase):

    """
    Test Accounts.
    """

    def test_init(self):

        """
        Test Account creation.
        """

        debit = Account(Account.Type.DEBIT)
        credit = Account(Account.Type.CREDIT)

    def test_credit_debit(self):

        """
        Test credit() and debit() of an Account.
        """

        cash = Account(Account.Type.ASSET)
        loan = Account(Account.Type.LIABILITY)
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
        Test increasing and decreasing of an Account.
        """

        cash = Account(Account.Type.ASSET)
        loan = Account(Account.Type.LIABILITY)
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
        Test naming accounts and annotating transactions.
        """

        cash = Account(Account.Type.DEBIT, name="My Wallet")
        loan = Account(Account.Type.CREDIT, name="My Loan")

        amount = Money("10000 EUR")
        cash.debit(amount, loan, note="Take the loan from my bank.")
        loan.debit(amount, cash, note="Pay back what I owe the bank.")
