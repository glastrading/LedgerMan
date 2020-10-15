class Money:
    defaultCurrency = "EUR"

    exchangeRates = []

    class ConversionError(Exception):
        pass

    # --- Convert currencies

    @staticmethod
    def addExchangeRate(exchangeRate):
        Money.exchangeRates += [exchangeRate]

    @staticmethod
    def canConvert(base, exchange):
        for e in Money.exchangeRates:
            if e.canConvert(base, exchange):
                return True
        return False

    def to(self, exchange):
        if self.currency == exchange:
            return self

        for e in Money.exchangeRates:
            if e.canConvert(self.currency, exchange):
                return e.convert(self)

        raise Money.ConversionError(
            "Can't convert " + self.currency + " to " + exchange + "."
        )

    # --- Constructor

    def __init__(self, amount=0, currency=defaultCurrency):
        self.amount = amount
        self.currency = currency

    # --- type conversions

    def __repr__(self):
        return str(self.amount) + " " + str(self.currency)

    def __int__(self):
        return self.amount

    def __truth__(self):
        return self.amount > 0

    # --- comparisons

    def __eq__(self, other):
        if type(other) in [int, float]:
            return self.amount == other
        elif type(other) == type(self):
            return self.amount == other.to(self.currency).amount
        else:
            raise TypeError(
                "Can't check equality of "
                + str(type(self))
                + " and "
                + str(type(other))
                + "."
            )

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if type(other) in [int, float]:
            return self.amount < other
        elif type(other) == type(self):
            return self.amount < other.to(self.currency).amount
        else:
            raise TypeError(
                "Can't compare " + str(type(self)) + " and " + str(type(other)) + "."
            )

    def __le__(self, other):
        if type(other) in [int, float]:
            return self.amount <= other
        elif type(other) == type(self):
            return self.amount <= other.to(self.currency).amount
        else:
            raise TypeError(
                "Can't compare " + str(type(self)) + " and " + str(type(other)) + "."
            )

    def __gt__(self, other):
        if type(other) in [int, float]:
            return self.amount > other
        elif type(other) == type(self):
            return self.amount > other.to(self.currency).amount
        else:
            raise TypeError(
                "Can't compare " + str(type(self)) + " and " + str(type(other)) + "."
            )

    def __ge__(self, other):
        if type(other) in [int, float]:
            return self.amount >= other
        elif type(other) == type(self):
            return self.amount >= other.to(self.currency).amount
        else:
            raise TypeError(
                "Can't compare " + str(type(self)) + " and " + str(type(other)) + "."
            )

    # --- calculations

    def __add__(self, other):
        if type(other) in [int, float]:
            return Money(self.amount + other, self.currency)
        elif type(other) == type(self):
            return Money(self.amount + other.to(self.currency).amount, self.currency)
        else:
            raise TypeError(
                "Can't add " + str(type(self)) + " and " + str(type(other)) + "."
            )

    def __sub__(self, other):
        if type(other) in [int, float]:
            return Money(self.amount - other, self.currency)
        elif type(other) == type(self):
            return Money(self.amount - other.to(self.currency).amount, self.currency)
        else:
            raise TypeError(
                "Can't subtract " + str(type(other)) + " from " + str(type(self)) + "."
            )

    def __neg__(self):
        return Money(-self.amount, self.currency)

    def __mul__(self, other):
        if type(other) in [int, float]:
            return Money(self.amount * other, self.currency)
        else:
            raise TypeError(
                "Can't multiply " + str(type(self)) + " by " + str(type(other)) + "."
            )

    def __truediv__(self, other):
        if type(other) in [int, float]:
            return Money(self.amount / other, self.currency)
        elif type(other) == type(self):
            return self.amount / other.to(self.currency).amount
        else:
            raise TypeError(
                "Can't divide " + str(type(self)) + " by " + str(type(other)) + "."
            )

    def __mod__(self, other):
        if type(other) in [int, float]:
            return Money(self.amount % other, self.currency)
        elif type(other) == type(self):
            return self.amount % other.to(self.currency).amount
        else:
            raise TypeError(
                "Can't mod " + str(type(self)) + " by " + str(type(other)) + "."
            )


class ExchangeRate:
    def __init__(self, base, exchange, rate):
        self.base = base
        self.exchange = exchange
        self.rate = rate

    def inverse(self):
        return ExchangeRate(self.exchange, self.base, 1 / self.rate)

    def __repr__(self):
        return str(Money(1, self.base)) + " => " + str(Money(self.rate, self.exchange))

    def canConvert(self, base, exchange):
        return (self.base == base and self.exchange == exchange) or (
            self.base == exchange and self.exchange == base
        )

    def convert(self, money):
        if type(money) == Money:
            if self.base == money.currency:
                return Money(money.amount * self.rate, self.exchange)
            elif self.exchange == money.currency:
                return Money(money.amount / self.rate, self.base)
            else:
                raise TypeError("Can't convert this currency here.")
        else:
            raise TypeError("Can't convert " + str(type(money)) + " to money.")
