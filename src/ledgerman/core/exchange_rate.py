import decimal
from .money import Money


class ExchangeRate:

    """
    Exchange Rates convert currencies.
    """

    def __init__(self, baseCurrency, destCurrency, rate):

        """
        Create an Exchange Rate.
        """

        self.baseCurrency = baseCurrency
        self.destCurrency = destCurrency
        self.rate = rate

    def __dict__(self):

        """
        Convert to a dictionary (storable, loadable).
        """

        return {"base": self.baseCurrency, "dest": self.destCurrency, "rate": self.rate}

    def __repr__(self):

        """
        Represent an Exchange Rate.
        """

        return str(self.__dict__())

    def inverse(self):

        """
        Invert the ExchangeRate (A=2B => B=1/2A).
        """

        return ExchangeRate(self.destCurrency, self.baseCurrency, 1 / self.rate)

    def getCurrencies(self):

        """
        Get the supported currency set.
        """

        return {self.baseCurrency, self.destCurrency}

    def getDest(self, baseCurrency=None):

        """
        Get the currency the Exchange Rate converts [baseCurrency] to.
        """

        if baseCurrency == None or self.baseCurrency == baseCurrency:
            return self.destCurrency
        elif self.destCurrency == baseCurrency:
            return self.baseCurrency

    def canConvert(self, baseCurrency, destCurrency=None):

        """
        Check if the ExchangeRate can convert between two currencies.
        """

        if destCurrency == None:
            return baseCurrency in self.getCurrencies()

        if baseCurrency == destCurrency and baseCurrency in self.getCurrencies():
            return True

        return self.getCurrencies() == {baseCurrency, destCurrency}

    def convert(self, money):

        """
        Convert money from one currency to another.
        """

        if not isinstance(money, Money):  # only money can be converted
            raise TypeError("Can't convert " + str(type(money)) + " to money.")

        if self.baseCurrency == money.currency:  # base -> dest
            return Money(
                str(
                    money.amount
                    * decimal.Decimal(self.rate).quantize(
                        decimal.Decimal(money.roundTo), rounding=decimal.ROUND_HALF_EVEN
                    )
                )
                + " "
                + self.destCurrency,
                roundTo=money.roundTo,
            )
        elif self.destCurrency == money.currency:  # base <- dest
            return Money(
                str(
                    money.amount
                    / decimal.Decimal(self.rate).quantize(
                        decimal.Decimal(money.roundTo), rounding=decimal.ROUND_HALF_EVEN
                    )
                )
                + " "
                + self.baseCurrency,
                roundTo=money.roundTo,
            )
        else:  # unknown currency
            raise TypeError(
                "Can't convert " + money.currency + " here (" + str(self) + ")."
            )

    def __eq__(self, other):

        """
        Check if two Exchange Rates are equal.
        """

        if not isinstance(other, ExchangeRate):
            return False

        if (
            self.rate == other.rate
            and self.baseCurrency == other.baseCurrency
            and self.destCurrency == other.destCurrency
        ):  # equality
            return True
        elif (
            self.rate == 1 / other.rate
            and self.baseCurrency == other.destCurrency
            and self.destCurrency == other.baseCurrency
        ):  # equality of the inverse
            return True

    def __hash__(self):

        """
        Hash an ExchangeRate. Needed for sets. Inverse has same hash.
        """

        hash1 = hash((self.rate, self.baseCurrency, self.destCurrency))
        hash2 = hash((1 / self.rate, self.destCurrency, self.baseCurrency))

        if hash1 > hash2:
            return hash1
        return hash2
