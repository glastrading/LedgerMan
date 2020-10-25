import decimal

from .exchange_rate_fetcher import ExchangeRateFetcher


class Money:

    """
    Money.
    """

    exchange = None

    @staticmethod
    def ensureExchangeExists():

        """
        The Money class has an associated Exchange. Ensure it exists.
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

    def to(self, currency):

        """
        Convert the Money object using the global money Exchange to another currency.
        """

        Money.ensureExchangeExists()
        return Money.exchange.convert(self, currency)

    def __init__(money, initArgument="0 EUR", roundTo="0.0001"):

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

        money.roundTo = roundTo
        money.amount = decimal.Decimal(moneyStringSplit[0])
        money.currency = moneyStringSplit[1]

    def __repr__(self):

        """
        Represent a Money object: '[amount] [currency]'.
        """

        return (
            str(
                self.amount.quantize(
                    decimal.Decimal(self.roundTo), rounding=decimal.ROUND_HALF_EVEN
                )
            )
            + " "
            + self.currency
        )

    # operations

    def __eq__(self, other):

        """
        Check equality of Money objects.
        """

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

        return Money() - self

    def __mul__(self, other):

        """
        Multiply Money objects by numbers.
        """

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
            other = decimal.Decimal(other).quantize(
                decimal.Decimal(self.roundTo), rounding=decimal.ROUND_HALF_EVEN
            )

        return Money(str(self.amount * other) + " " + self.currency)

    def __truediv__(self, other):

        """
        Divide Money objects by numbers or others.
        """

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


decimal.getcontext().prec = 128  # general max precision
