from ledgerman import *


class TradeAccount:
    """
    TradeAccounts are used to do accounting for a currency trading.
    """

    def __init__(obj, base, asset):
        """
        Create a TradeAccount object.
        """

        obj.base = base
        obj.asset = asset

        obj.expense = Money(0, base)  # using base
        obj.balance = Money(0, asset)  # asset is bought

        obj.transactions = []

    def __repr__(obj):
        """
        Represent a TradeAccount.
        """

        repr = "TradeAccount {\n"
        repr += "\t" + obj.base + " -> " + obj.asset + "\n"
        repr += "\tbalance = " + str(obj.balance) + "\n"
        repr += "\t\t= " + str(obj.balance.to(obj.base)) + "\n"
        repr += "\texpense = " + str(obj.expense) + "\n"
        repr += "\tprofits = " + str(obj.getProfits()) + "\n"
        repr += "}"

        return repr

    def trade(obj, expense, received=None, date=""):
        """
        Trade expense (base currency) to received (asset currency).
        """

        if type(received) == type(None):
            received = expense.to(obj.asset)

        obj.expense += expense
        obj.balance += received

        obj.transactions += (expense, received, date)

    def take(obj, asset, date=""):
        """
        Take some of the asset away.
        """

        obj.balance -= asset

    def put(obj, asset, date=""):
        """
        Add some to the asset.
        """

        obj.balance += asset

    def getProfits(obj):
        """
        Calculate profits.
        """

        return -obj.expense + obj.balance
