from unittest import TestCase

from ledgerman import *


class TestAccounts(TestCase):
    """
    Tests related to the Account class.
    """

    def test_init_empty(self):
        """
        Test Account().
        """
        a = Account()
        self.assertEqual(
            a.name, "Account", "Default Account names should be 'Account'."
        )

    def test_init_name(self):
        """
        Test Account(name).
        """
        a = Account("BankAccount")
        self.assertEqual(
            a.name, "BankAccount", "Account names should be stored properly."
        )

    def test_init_currency(self):
        """
        Test Account(name, currency).
        """
        a = Account("MyBitcoinWallet", "BTC")
        self.assertEqual(a.balance, 0, "Account balances should be 0 by default.")
        self.assertEqual(
            a.balance.currency, "BTC", "Account currencies should be stored properly."
        )

    def test_init_full(self):
        """
        Test Account(name, money).
        """
        a = Account("BankAccount", Money(5000, "EUR"))
        self.assertEqual(
            a.name, "BankAccount", "Account names should be stored properly."
        )
        self.assertEqual(a.balance, 5000, "Account balances should be stored properly.")
