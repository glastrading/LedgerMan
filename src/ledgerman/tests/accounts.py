from unittest import TestCase

from ledgerman import *


class TestAccounts(TestCase):
    def test_init_empty(self):
        a = Account()
        self.assertEqual(
            a.name, "Account", "Default Account names should be 'Account'."
        )

    def test_init_name(self):
        a = Account("BankAccount")
        self.assertEqual(
            a.name, "BankAccount", "Account names should be stored properly."
        )

    def test_init_full(self):
        a = Account("BankAccount", Money(5000, "EUR"))
        self.assertEqual(
            a.name, "BankAccount", "Account names should be stored properly."
        )
        self.assertEqual(a.balance, 5000, "Account balances should be stored properly.")
