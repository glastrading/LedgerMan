from .money import Money


class Account:
    """
    The Account class stores and tracks Money.
    """

    def __init__(obj, name="Account", balance=Money(0), record=""):
        """
        Create an Account object.
        """
        obj.name = name
        if type(balance) in [int, float]:
            balance = Money(balance)
        obj.balance = balance
        obj.record = record

    def __repr__(obj):
        """
        Represent an Account.
        """
        return "{ " + obj.name + " (" + str(obj.balance) + ") }"

    # TODO: operations
