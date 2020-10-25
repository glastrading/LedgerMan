from ..core.money import Money
from .journal import Journal


class Account:

    """
    Accounts keep track of money on it.
    """

    class Type:

        """
        The account type defines which actions increase the account.
        Debit accounts increase on debit, Credit accounts on credit.
        """

        # Account(Type.DEBIT) * DEBIT == Account(Type.CREDIT) * CREDIT == 1
        DEBIT = 1
        CREDIT = -1

        ASSET = DEBIT
        DRAW = DEBIT
        EXPENSE = DEBIT

        LIABILITY = CREDIT
        EQUITY = CREDIT
        REVENUE = CREDIT

    def __init__(self, type, startBalance="0 EUR", name="Account"):

        """
        Create an Account.
        """

        if type not in {Account.Type.DEBIT, Account.Type.CREDIT}:
            raise ValueError("Accounts can only be Debit (1) or Credit (-1).")

        if isinstance(startBalance, str):
            if len(startBalance.split(" ")) == 2:
                startBalance = Money(startBalance)
            elif len(startBalance.split(" ")) == 1:
                startBalance = Money("0 " + startBalance)
            else:
                raise ValueError(
                    "Unexpected long string input for an account: '"
                    + startBalance
                    + "'"
                )

        self.journal = Journal()

        self.balance = startBalance
        self.currency = self.balance.currency

        self.type = type
        self.name = name

    def __dict__(self):
        return {
            "name": self.name,
            "type": {1: "debit", -1: "credit"}[self.type],
            "balance": self.balance,
        }

    def __repr__(self):
        return self.name + " (" + {1: "debit", -1: "credit"}[self.type] + ")"

    def transaction(self, type, amount, other, date=None, note="", mirror=False):

        """
        Move money beween Accounts.
        """

        if isinstance(amount, str):
            amount = Money(amount)

        sign = self.type * type  # if they are equal -> 1 else -1

        self.balance += amount * sign

        if type == Account.Type.DEBIT:
            self.journal.log(
                type, self.balance, amount, self, other, date=date, note=note
            )
        elif type == Account.Type.CREDIT:
            self.journal.log(
                type, self.balance, amount, other, self, date=date, note=note
            )
        else:
            raise ValueError("Transactions need to be DEBIT or CREDIT.")

        if mirror:
            other.transaction(
                type * -1, amount, self, date=date, note=note, mirror=False
            )

    def credit(self, amount, debitFrom, date=None, note="", mirror=True):

        """
        Increase the Account if it is a credit-type account.
        """

        self.transaction(
            Account.Type.CREDIT,
            amount,
            debitFrom,
            date=date,
            note=note,
            mirror=mirror,
        )

    def debit(self, amount, creditFrom, date=None, note="", mirror=True):

        """
        Increase the Account if it is a debit-type account.
        """

        self.transaction(
            Account.Type.DEBIT,
            amount,
            creditFrom,
            date=date,
            note=note,
            mirror=mirror,
        )

    def increase(self, amount, other, date=None, note="", mirror=True):

        """
        Increasing means that if the account is debit, it will be debited,
        if it is credit, credited.
        """

        self.transaction(self.type, amount, other, date=None, note=note, mirror=mirror)

    def decrease(self, amount, other, date=None, note="", mirror=True):

        """
        Decreasing means that if the account is debit, it will be credited,
        if it is credit, debited.
        """

        self.transaction(
            self.type * -1, amount, other, date=None, note=note, mirror=mirror
        )
