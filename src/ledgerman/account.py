from .money import Money

# Accounts store and track money.


class Account:
    def __init__(obj, name="Account", balance=Money(0), record=""):
        obj.name = name
        if type(balance) in [int, float]:
            balance = Money(balance)
        obj.balance = balance
        obj.record = record

    def __repr__(obj):
        return "{ " + obj.name + " (" + str(obj.balance) + ") }"

    # TODO: operations
