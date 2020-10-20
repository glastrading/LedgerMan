# LedgerMans representation of money.


class Money:
    defaultCurrency = "EUR"
    exchange = None

    # --- Convert currencies

    @staticmethod
    def ensureExchangeExists():
        if Money.exchange == None:
            from .exchange import Exchange

            Money.exchange = Exchange()

    @staticmethod
    def addExchangeRate(*exchangeRate):
        Money.ensureExchangeExists()
        Money.exchange.insertExchangeRate(*exchangeRate)

    @staticmethod
    def canConvert(base, other):
        Money.ensureExchangeExists()
        return Money.exchange.canConvert(base, other)

    def to(obj, currency):
        Money.ensureExchangeExists()
        return Money.exchange.convert(obj, currency)

    # --- Constructor

    def __init__(obj, amount=0, currency=defaultCurrency):
        obj.amount = amount
        obj.currency = currency

    # --- type conversions

    def __repr__(obj):
        return str(obj.amount) + " " + str(obj.currency)

    def __int__(obj):
        return obj.amount

    def __truth__(obj):
        return obj.amount > 0

    # --- comparisons

    def __eq__(obj, other):
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
        if type(other) in [int, float]:
            return obj.amount > other
        elif type(other) == type(obj):
            return obj.amount > other.to(obj.currency).amount
        else:
            raise TypeError(
                "Can't compare " + str(type(obj)) + " and " + str(type(other)) + "."
            )

    def __ge__(obj, other):
        if type(other) in [int, float]:
            return obj.amount >= other
        elif type(other) == type(obj):
            return obj.amount >= other.to(obj.currency).amount
        else:
            raise TypeError(
                "Can't compare " + str(type(obj)) + " and " + str(type(other)) + "."
            )

    # --- calculations

    def __add__(obj, other):
        if type(other) in [int, float]:
            return Money(obj.amount + other, obj.currency)
        elif type(other) == type(obj):
            return Money(obj.amount + other.to(obj.currency).amount, obj.currency)
        else:
            raise TypeError(
                "Can't add " + str(type(obj)) + " and " + str(type(other)) + "."
            )

    def __sub__(obj, other):
        if type(other) in [int, float]:
            return Money(obj.amount - other, obj.currency)
        elif type(other) == type(obj):
            return Money(obj.amount - other.to(obj.currency).amount, obj.currency)
        else:
            raise TypeError(
                "Can't subtract " + str(type(other)) + " from " + str(type(obj)) + "."
            )

    def __neg__(obj):
        return Money(-obj.amount, obj.currency)

    def __mul__(obj, other):
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
        if type(other) in [int, float]:
            return Money(obj.amount / other, obj.currency)
        elif type(other) == type(obj):
            return obj.amount / other.to(obj.currency).amount
        else:
            raise TypeError(
                "Can't divide " + str(type(obj)) + " by " + str(type(other)) + "."
            )

    def __mod__(obj, other):
        if type(other) in [int, float]:
            return Money(obj.amount % other, obj.currency)
        elif type(other) == type(obj):
            return obj.amount % other.to(obj.currency).amount
        else:
            raise TypeError(
                "Can't mod " + str(type(obj)) + " by " + str(type(other)) + "."
            )
