from .money import Money

# ExchangeRates convert money of different currencies.


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
        if base == other and base in obj.getCurrencies():
            return True

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


# Exchanges are collections of ExchangeRates.


class Exchange:
    def __init__(obj, *exchangeRates):
        obj.exchangeRates = []
        for exchangeRate in exchangeRates:
            if type(exchangeRate) == ExchangeRate:
                obj.insertExchangeRate(exchangeRate)
            elif type(exchangeRate) in [list, tuple]:
                obj.insertExchangeRate(*exchangeRate)
            else:
                raise TypeError("Unknow type for an exchangeRate.")

    def __repr__(obj):
        if len(obj):
            return "{" + "; ".join([str(e) for e in obj.exchangeRates]) + "}"
        else:
            return "{ Empty Exchange }"

    def __len__(obj):
        return len(obj.exchangeRates)

    # checks

    def canConvert(obj, base, other=""):
        for exchangeRate in obj.exchangeRates:
            if exchangeRate.canConvert(base, other):
                return True

        if other == "":
            return False

        for exchangeRate1 in obj.exchangeRates:  # CB
            for exchangeRate2 in obj.exchangeRates:  # AB
                if not exchangeRate1.canConvert(base, exchangeRate2.base):  # CB C, B
                    continue
                if not exchangeRate2.canConvert(exchangeRate2.base, other):  # AB A, A
                    continue
                return True

        return False

    # modify Exchanges

    def insertExchangeRate(obj, *args):  # update / append a rate
        if len(args) == 1:  # rate
            obj.exchangeRates += [args[0]]
        elif len(args) == 3:  # base, other, rate
            obj.exchangeRates += [ExchangeRate(args[0], args[1], args[2])]
        else:
            raise ValueError("Invalid exchange rate for Exchange.insertExchangeRate().")

    # transform Money

    def convert(obj, money, destinationCurrency):
        if type(money) != Money:  # only money can be converted
            raise TypeError("Can't convert " + str(type(money)) + " to money.")

        if money.currency == destinationCurrency:
            return money

        # Primary conversions (a -> b)
        for exchangeRate in obj.exchangeRates:
            if exchangeRate.canConvert(money.currency, destinationCurrency):
                return exchangeRate * money

        # Secondary conversions (a -> m -> b)
        for exchangeRate1 in obj.exchangeRates:
            for exchangeRate2 in obj.exchangeRates:
                if not exchangeRate1.canConvert(money.currency, exchangeRate2.base):
                    continue
                if not exchangeRate2.canConvert(
                    exchangeRate2.base, destinationCurrency
                ):
                    continue
                return exchangeRate2 * (exchangeRate1 * money)

        # Tertiary conversions (a -> m1 -> m2 -> b) are not implemented

        # unknown currency
        raise TypeError("Can't convert the currency using this Exchange.")
