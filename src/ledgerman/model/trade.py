from ..core.account import Account
from ..core.money import Money


class Trade:

    """
    Trades represent currency-pair trades (with a broker).
    """

    # --- DATA MODEL METHODS --- #

    def __init__(self, baseCurrency, assetCurrency):

        """
        Create a Trade.
        """

        self.expense = Account(
            "expense", baseCurrency, name="Expense in " + baseCurrency
        )
        self.asset = Account(
            "asset", assetCurrency, name="Traded Asset in " + assetCurrency
        )

        self.baseCurrency = baseCurrency
        self.assetCurrency = assetCurrency

    def __repr__(self):

        """
        Represent a Trade.
        """

        repr = "Trade {\n"
        repr += "\t" + self.baseCurrency + " -> " + self.assetCurrency + "\n"
        repr += "\tbalance = " + str(self.asset.balance) + "\n"
        repr += "\t\t= " + str(self.asset.balance.to(self.baseCurrency)) + "\n"
        repr += "\texpense = " + str(self.expense.balance) + "\n"
        repr += "\tprofits = " + str(self.getProfits()) + "\n"
        repr += "}"

        return repr

    # --- CLASS SPECIFIC METHODS --- #

    def trade(self, expense, received=None, date=None):

        """
        Trade expense (base currency) to received (asset currency).
        """

        if type(received) == type(None):
            received = expense.to(self.assetCurrency)

        self.expense.increase(expense, self.asset, date=date, mirror=False)
        self.asset.increase(received, self.expense, date=date, mirror=False)

    def take(self, amount, date=None):

        """
        Take some of the asset away.
        """

        self.asset.decrease(amount, self.expense, date=date, mirror=False)

    def put(self, amount, date=None):

        """
        Add some to the asset.
        """

        self.asset.increase(amount, self.expense, date=date, mirror=False)

    def getProfits(self):

        """
        Calculate the current profits.
        """

        return self.asset.balance - self.expense.balance
