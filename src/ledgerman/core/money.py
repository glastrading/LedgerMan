import decimal
import json

from .exchange_rate_fetcher import ExchangeRateFetcher


class Money:

    """
    Money.
    """

    # --- STATIC VARIABLES --- #

    exchange = None

    # --- STATIC METHODS --- #

    @staticmethod
    def ensureExchangeExists():

        """
        The Money class has an associated Exchange. Make sure it exists.
        """

        if Money.exchange == None:
            from .exchange import Exchange

            Money.exchange = Exchange()

    @staticmethod
    def insertExchangeRate(*exchangeRate):

        """
        Add an ExchangeRate to the global money Exchange.
        """

        Money.ensureExchangeExists()
        Money.exchange.insertExchangeRate(*exchangeRate)

    @staticmethod
    def canConvert(base, other):

        """
        Check if the money Exchange can convert from a base currency to another.
        """

        Money.ensureExchangeExists()
        return Money.exchange.canConvert(base, other)

    @staticmethod
    def fetchRates(source="ecb", verbose=False):

        """
        Fetch ExchangeRates from a source api.
        """

        for e in ExchangeRateFetcher.fetch(source, verbose):
            Money.insertExchangeRate(*e)

    # --- DATA MODEL METHODS --- #

    def __init__(self, initArgument="0 EUR", precision=8):

        """
        Create a Money object.
        """

        if not isinstance(initArgument, str):
            raise TypeError(
                "Did not expect this type to initialise 'Money': "
                + str(type(initArgument))
            )

        moneyString = initArgument
        moneyStringSplit = moneyString.split(" ")

        if len(moneyStringSplit) != 2:
            raise ValueError(
                "Expected a money string of the format '[amount] [currency]'."
            )

        self.precision = precision + 1
        decimal.getcontext().prec = self.precision
        self.amount = decimal.Decimal(moneyStringSplit[0]) * decimal.Decimal(1)
        self.currency = moneyStringSplit[1]

    def __repr__(self):

        """
        Represent a Money object: '[amount] [currency]'.
        """

        decimal.getcontext().prec = self.precision
        return "{:f}".format(self.amount.normalize()) + " " + self.currency

    # --- SERIALIZATION METHODS --- #

    def serialize(self, indent=4, sort_keys=True):
        d = {
            "_type": "Money",
            "amount": "{:f}".format(self.amount),
            "currency": self.currency,
            "precision": self.precision - 1,
        }

        return json.dumps(d, indent=indent, sort_keys=sort_keys)

    @staticmethod
    def deserialize(d):
        if isinstance(d, str):
            d = json.loads(d)

        if d["_type"] != "Money":
            raise ValueError("Cannot deserialize objects other than Money.")

        return Money(d["amount"] + " " + d["currency"], d["precision"])

    # --- CLASS SPECIFIC METHODS --- #

    def to(self, currency):

        """
        Convert the Money object using the global money Exchange to another currency.
        """

        Money.ensureExchangeExists()
        return Money.exchange.convert(self, currency)

    def smallest(self):
        decimal.getcontext().prec = self.precision
        return decimal.Decimal("0." + self.precision * "0" + "1")

    # --- DATA MODEL OPERATIONS --- #

    def __eq__(self, other):

        """
        Check equality of Money objects.
        """

        decimal.getcontext().prec = self.precision

        if not isinstance(other, Money):
            raise TypeError(
                "unsupported operand type(s) for ==: 'Money' and '"
                + type(other).__name__
                + "'"
            )

        return other.to(self.currency).amount == self.amount

    def __add__(self, other):

        """
        Add Money objects.
        """

        decimal.getcontext().prec = self.precision

        if not isinstance(other, Money):
            raise TypeError(
                "unsupported operand type(s) for +: 'Money' and '"
                + type(other).__name__
                + "'"
            )

        return Money(
            str(self.amount + other.to(self.currency).amount) + " " + self.currency
        )

    def __sub__(self, other):

        """
        Subtract Money objects.
        """

        decimal.getcontext().prec = self.precision

        if not isinstance(self, Money):
            raise TypeError(
                "unsupported operand type(s) for -: 'Money' and '"
                + type(other).__name__
                + "'"
            )

        return Money(
            str(self.amount - other.to(self.currency).amount) + " " + self.currency
        )

    def __neg__(self):

        """
        Negate Money objects.
        """

        decimal.getcontext().prec = self.precision

        return Money() - self

    def __mul__(self, other):

        """
        Multiply Money objects by numbers.
        """

        decimal.getcontext().prec = self.precision

        if (
            not isinstance(other, float)
            and not isinstance(other, int)
            and not isinstance(other, decimal.Decimal)
        ):
            raise TypeError(
                "unsupported operand type(s) for *: 'Money' and '"
                + type(other).__name__
                + "'"
            )

        if isinstance(other, float):  # make sure it is rounded properly
            other = decimal.Decimal(other)

        return Money(str(self.amount * other) + " " + self.currency)

    def __truediv__(self, other):

        """
        Divide Money objects by numbers or others.
        """

        decimal.getcontext().prec = self.precision

        if (
            not isinstance(other, float)
            and not isinstance(other, int)
            and not isinstance(other, decimal.Decimal)
            and not isinstance(other, Money)
        ):
            raise TypeError(
                "unsupported operand type(s) for *: 'Money' and '"
                + type(other).__name__
                + "'"
            )

        if isinstance(other, float):
            other = decimal.Decimal(other)
        if isinstance(other, Money):
            return self.amount / other.to(self.currency).amount

        return Money(str(self.amount / other) + " " + self.currency)
