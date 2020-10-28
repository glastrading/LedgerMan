from .trade import Trade
from ..core.money import Money


class TradeAccount:

    """
    TradeAccounts can record many trades of different currencies.
    """

    # --- DATA MODEL METHODS --- #

    def __init__(self, baseCurrency="EUR"):

        """
        Create a TradeAccount.
        """

        self.trades = []

    # --- CLASS SPECIFIC METHODS --- #

    def findTrade(self, baseCurrency, assetCurrency):

        """
        Find a trade corresponding to a currency-pair.
        """

        for t in self.trades:
            if t.baseCurrency == baseCurrency and t.assetCurrency == assetCurrency:
                return t
        return None

    def trade(self, expense, received, date=None):

        """
        Trade with existing or new trades within the TradeAccount.
        """

        if isinstance(expense, str):
            expense = Money(expense)
        if isinstance(received, str):
            received = Money(received)

        tradeExists = True
        trade = self.findTrade(expense.currency, received.currency)

        if type(trade) == type(None):
            trade = Trade(expense.currency, received.currency)
            tradeExists = False

        trade.trade(expense, received, date=date)

        if not tradeExists:
            self.trades += [trade]

    def take(self, amount, date=None):

        """
        Take some of the asset away.
        """

        if isinstance(amount, str):
            amount = Money(amount)

        trade = self.findTrade("EUR", amount.currency)
        trade.asset.decrease(amount, trade.expense, date=date, mirror=False)

    def put(self, amount, date=None):

        """
        Add some to the asset.
        """

        if isinstance(amount, str):
            amount = Money(amount)

        trade = self.findTrade("EUR", amount.currency)
        trade.asset.increase(amount, trade.expense, date=date, mirror=False)

    def getBalance(self):

        """
        Calculate the assets balance over all trades.
        """

        balance = Money("0 EUR")

        for trade in self.trades:
            balance += trade.asset.balance

        return balance

    def getExpense(self):

        """
        Calculate the expense over all trades.
        """

        expense = Money("0 EUR")

        for trade in self.trades:
            expense += trade.expense.balance

        return expense

    def getProfits(self):

        """
        Calculate the current profits of all trades.
        """

        return self.getBalance() - self.getExpense()
