from jcdb import Object


class Ledger(Object):

    """
    Ledgers store account data and metadata.
    """

    # --- DATA MODEL METHODS --- #

    def __init__(self, name="New Ledger", *accounts):

        """
        Create a Ledger.
        """

        # check name
        if type(name).__name__ != "str":
            raise TypeError("Unexpected Type for 'Ledger.name': " + type(name).__name__)

        self.name = name

        # check accounts
        for n in range(len(accounts)):
            a = accounts[n]
            if type(a).__name__ != "Account":
                raise TypeError(
                    "Unexpected Type for 'Ledger.accounts["
                    + n
                    + "]': "
                    + type(a).__name__
                )

        self.accounts = list(accounts)

    def __repr__(self):
        return "<Ledger '" + self.name + "'>"

    # --- DATA MODEL OPERATIONS --- #

    def __len__(self):
        return len(self.accounts)


Object.register(Ledger)
