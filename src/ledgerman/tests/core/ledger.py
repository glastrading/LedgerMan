from unittest import TestCase

from ledgerman import *


class TestLedger(TestCase):

    """
    Test Ledgers.
    """

    def test_init(self):

        """
        Ledger: Test initialization
        """

        ledger = Ledger("My personal Ledger 2020")

    def test_serialization(self):

        """
        Ledger: Test serialization
        """

        l1 = Ledger()
        l2 = Ledger.decode(l1.encode())

        self.assertEquals(l1, l2)
