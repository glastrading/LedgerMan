from unittest import TestCase

from ledgerman import *


class TestJournal(TestCase):

    """
    Test Journals.
    """

    def test_init(self):

        """
        Journal: Test initialization
        """

        Journal()

    def test_serialization(self):

        """
        Journal: Test serialization
        """

        j1 = Journal()
        j2 = Journal.deserialize(j1.serialize())

        self.assertEquals(j1, j2)
