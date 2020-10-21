from .fetch import ExchangeRateFetcher


class Money:
    """
    Money has an amount and a currency. It is a core type to be acted upon.
    """

    defaultCurrency = "EUR"
    exchange = None

    # --- Convert currencies

    @staticmethod
    def ensureExchangeExists():
        """
        The Money class has an associated Exchange. Ensure it exists.
        """
        if Money.exchange == None:
            from .exchange import Exchange

            Money.exchange = Exchange()

    @staticmethod
    def addExchangeRate(*exchangeRate):
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
            Money.addExchangeRate(*e)

    def to(obj, currency):
        """
        Convert the Money object using the global money Exchange to another currency.
        """
        Money.ensureExchangeExists()
        return Money.exchange.convert(obj, currency)

    # --- Constructor

    def __init__(obj, amount=0, currency=defaultCurrency):
        """
        Create a Money object.
        """
        obj.amount = amount
        obj.currency = currency

    # --- type conversions

    def __repr__(obj):
        """
        A common representation of Money.
        """
        return str(obj.amount) + " " + str(obj.currency)

    def __int__(obj):
        """
        Get the Money's amount.
        """
        return obj.amount

    def __truth__(obj):
        """
        True if there is an amount of Money stored.
        """
        return obj.amount > 0

    # --- comparisons

    def __eq__(obj, other):
        """
        Check for equality of Money and another Money's amount or a number.
        Also converts to the necessary currency.
        """
        if type(other) in [int, float]:
            return obj.amount == other
        elif type(other) == type(obj):
            return obj.amount == other.to(obj.currency).amount
        else:
            raise TypeError(
                "Can't check equality of "
                + str(type(obj))
                + " and "
                + str(type(other))
                + "."
            )

    def __ne__(obj, other):
        return not obj == other

    def __lt__(obj, other):
        if type(other) in [int, float]:
            return obj.amount < other
        elif type(other) == type(obj):
            return obj.amount < other.to(obj.currency).amount
        else:
            raise TypeError(
                "Can't compare " + str(type(obj)) + " and " + str(type(other)) + "."
            )

    def __le__(obj, other):
        if type(other) in [int, float]:
            return obj.amount <= other
        elif type(other) == type(obj):
            return obj.amount <= other.to(obj.currency).amount
        else:
            raise TypeError(
                "Can't compare " + str(type(obj)) + " and " + str(type(other)) + "."
            )

    def __gt__(obj, other):
        return not obj <= other

    def __ge__(obj, other):
        return not obj < other

    # --- calculations

    def __add__(obj, other):
        """
        Add Money objects (auto-conversion) or numbers to money.
        """
        if type(other) in [int, float]:
            return Money(obj.amount + other, obj.currency)
        elif type(other) == type(obj):
            return Money(obj.amount + other.to(obj.currency).amount, obj.currency)
        else:
            raise TypeError(
                "Can't add " + str(type(obj)) + " and " + str(type(other)) + "."
            )

    def __sub__(obj, other):
        """
        Subract Money objects (auto-conversion) or numbers from money.
        """
        return obj + (-other)

    def __neg__(obj):
        """
        Negate the Money's amount.
        """
        return Money(-obj.amount, obj.currency)

    def __mul__(obj, other):
        """
        Multiplie Money by a number (not by Money).
        When multiplied by an ExchangeRate, the Money is converted by it.
        """
        from .exchange import ExchangeRate

        if type(other) == ExchangeRate:
            return other * obj  # conversion
        elif type(other) in [int, float]:
            return Money(obj.amount * other, obj.currency)
        else:
            raise TypeError(
                "Can't multiply " + str(type(obj)) + " by " + str(type(other)) + "."
            )

    def __truediv__(obj, other):
        """
        Divide Money by a number (=> Money) or Money (=> Number).
        """
        if type(other) in [int, float]:
            return Money(obj.amount / other, obj.currency)
        elif type(other) == type(obj):
            return obj.amount / other.to(obj.currency).amount
        else:
            raise TypeError(
                "Can't divide " + str(type(obj)) + " by " + str(type(other)) + "."
            )

    def __mod__(obj, other):
        """
        Return the leftover number when dividing money by an integer.
        """
        if type(other) in [int, float]:
            return Money(obj.amount % other, obj.currency)
        elif type(other) == type(obj):
            return obj.amount % other.to(obj.currency).amount
        else:
            raise TypeError(
                "Can't mod " + str(type(obj)) + " by " + str(type(other)) + "."
            )
