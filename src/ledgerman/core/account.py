import json

from .money import Money
from .journal import Journal


class Account:

    """
    Accounts keep track of money on it.
    """

    # --- STATIC VARIABLES --- #

    DEBIT = 1
    CREDIT = -1

    # --- STATIC METHODS --- #

    @staticmethod
    def typeToInt(type):

        """
        The account type defines which actions increase the account.
        Debit accounts increase on debit, Credit accounts on credit.
        """

        if isinstance(type, str):
            try:
                type = {
                    "debit": Account.DEBIT,
                    "credit": Account.CREDIT,
                    "asset": Account.DEBIT,
                    "draw": Account.DEBIT,
                    "expense": Account.DEBIT,
                    "liability": Account.CREDIT,
                    "equity": Account.CREDIT,
                    "revenue": Account.CREDIT,
                }[type.lower()]
            except KeyError:
                raise ValueError("Unknown account type.")

        if type in {Account.CREDIT, Account.DEBIT}:
            return type
        else:
            raise ValueError("Unrecognized integer account type: " + str(type))

        return type

    # --- DATA MODEL METHODS --- #

    def __init__(self, type, balance="0 EUR", journal=None, name="Account"):

        """
        Create an Account.
        """

        self.typeInt = Account.typeToInt(type)  # will fail for wrong input

        if isinstance(balance, str):
            if len(balance.split(" ")) == 2:
                balance = Money(balance)
            elif len(balance.split(" ")) == 1:
                balance = Money("0 " + balance)
            else:
                raise ValueError(
                    "Unexpected long string input for an account: '" + balance + "'"
                )

        if journal != None:
            self.journal = journal
        else:
            self.journal = Journal()

        self.balance = balance
        self.currency = self.balance.currency

        self.type = type
        self.name = name

    def __repr__(self):
        return self.serialize()

    # --- SERIALIZATION METHODS --- #

    def serialize(self, indent=4, sort_keys=True):
        d = {
            "_type": "Account",
            "name": self.name,
            "type": self.type,
            "balance": json.loads(self.balance.serialize()),
            "journal": json.loads(self.journal.serialize()),
        }

        return json.dumps(d, indent=indent, sort_keys=sort_keys)

    @staticmethod
    def deserialize(d):
        if isinstance(d, str):
            d = json.loads(d)

        if d["_type"] != "Account":
            raise ValueError("Cannot deserialize objects other than Account.")

        journal = Journal.deserialize(d["journal"])
        balance = Money.deserialize(d["balance"])

        return Account(d["type"], balance=balance, journal=journal)

    # --- CLASS SPECIFIC METHODS --- #

    def transaction(self, type, amount, other, date=None, note="", mirror=False):

        """
        Move money beween Accounts.
        """

        if isinstance(amount, str):
            amount = Money(amount)

        sign = self.typeInt * self.typeToInt(type)  # if they are equal -> 1 else -1

        self.balance += amount * sign

        if self.typeToInt(type) == Account.DEBIT:
            self.journal.log(
                type, self.balance, amount, self, other, date=date, note=note
            )
        elif self.typeToInt(type) == Account.CREDIT:
            self.journal.log(
                type, self.balance, amount, other, self, date=date, note=note
            )
        else:
            raise ValueError("Transactions need to be DEBIT or CREDIT.")

        if mirror:
            other.transaction(
                self.typeToInt(type) * -1,
                amount,
                self,
                date=date,
                note=note,
                mirror=False,
            )

    def credit(self, amount, debitFrom, date=None, note="", mirror=True):

        """
        Increase the Account if it is a credit-type account.
        """

        self.transaction(
            "credit",
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
            "debit",
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

        self.transaction(
            self.typeInt, amount, other, date=None, note=note, mirror=mirror
        )

    def decrease(self, amount, other, date=None, note="", mirror=True):

        """
        Decreasing means that if the account is debit, it will be credited,
        if it is credit, debited.
        """

        self.transaction(
            self.typeInt * -1, amount, other, date=None, note=note, mirror=mirror
        )

    # --- DATA MODEL OPERATIONS --- #

    def __eq__(self, other):
        if type(other) != Account:
            return False
        return (
            self.name == other.name
            and self.type == other.type
            and self.balance == other.balance
            and self.journal == other.journal
        )
