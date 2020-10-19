from .money import Money


class ExchangeRate:
    def __init__(obj, base, other, rate):  # 1 * base = rate * other
        obj.base = base
        obj.other = other
        obj.rate = rate

    def __repr__(obj):
        return str(Money(1, obj.base)) + " => " + str(Money(obj.rate, obj.other))

    # transform the ExchangeRate

    def inverse(obj):
        return ExchangeRate(obj.other, obj.base, 1 / obj.rate)

    # checks and getters

    def getCurrencies(obj):
        return {obj.base, obj.other}

    def canConvert(obj, base, other=""):
        if other == "":
            return base in obj.getCurrencies()

        return obj.getCurrencies() == {base, other}

    # transform some Money

    def convert(obj, money):
        if type(money) != Money:  # only money can be converted
            raise TypeError("Can't convert " + str(type(money)) + " to money.")

        if obj.base == money.currency:  # base -> other
            return Money(money.amount * obj.rate, obj.other)
        elif obj.other == money.currency:  # base <- other
            return Money(money.amount / obj.rate, obj.base)
        else:  # unknown currency
            raise TypeError("Can't convert this currency here.")

    def __mul__(obj, money):  # Money() * ExchangeRate() = convertedMoney
        if type(money) != Money:
            raise TypeError("Can't multiply ExchangeRates by anything but money.")

        return obj.convert(money)
