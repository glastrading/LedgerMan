from ..core.money import Money


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
            startBalance = Money(startBalance)

        self.balance = startBalance
        self.type = type
        self.name = name

    def __repr__(self):
        return str({"name": self.name, "type": self.type, "balance": self.balance})

    def transaction(self, type, amount, other, note="", done=False):

        """
        Move money beween Accounts.
        """

        sign = self.type * type  # if they are equal -> 1 else -1

        self.balance += amount * sign

        if not done:
            other.transaction(type * -1, amount, self, note, done=True)

    def credit(self, amount, debitFrom, note=""):

        """
        Increase the Account if it is a credit-type account.
        """

        self.transaction(Account.Type.CREDIT, amount, debitFrom, note)

    def debit(self, amount, creditFrom, note=""):

        """
        Increase the Account if it is a debit-type account.
        """

        self.transaction(Account.Type.DEBIT, amount, creditFrom, note)

    def increase(self, amount, other, note=""):

        """
        Increasing means that if the account is debit, it will be debited,
        if it is credit, credited.
        """

        self.transaction(self.type, amount, other, note)

    def decrease(self, amount, other, note=""):

        """
        Decreasing means that if the account is debit, it will be credited,
        if it is credit, debited.
        """

        self.transaction(self.type * -1, amount, other, note)
