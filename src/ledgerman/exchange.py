from .money import Money


class ExchangeRate:
    """
    ExchangeRates convert Money of different currencies.
    """

    def __init__(obj, base, other, rate):  # 1 * base = rate * other
        """
        Create an ExchangeRate object.
        """
        obj.base = base
        obj.other = other
        obj.rate = rate

    def __repr__(obj):
        """
        A common representation of an ExchangeRate.
        """
        return str(Money(1, obj.base)) + " => " + str(Money(obj.rate, obj.other))

    # transform the ExchangeRate

    def inverse(obj):
        """
        Invert the ExchangeRate (A=2B => B=1/2A).
        """
        return ExchangeRate(obj.other, obj.base, 1 / obj.rate)

    # checks and getters

    def getCurrencies(obj):
        return {obj.base, obj.other}

    def getOther(obj, base):
        if obj.base == base:
            return obj.other
        elif obj.other == base:
            return obj.base

    def canConvert(obj, base, other=""):
        """
        Check if the ExchangeRate can convert between two currencies.
        """
        if base == other and base in obj.getCurrencies():
            return True

        if other == "":
            return base in obj.getCurrencies()

        return obj.getCurrencies() == {base, other}

    # transform some Money

    def convert(obj, money):
        """
        Convert money from one currency to another.
        """
        if type(money) != Money:  # only money can be converted
            raise TypeError("Can't convert " + str(type(money)) + " to money.")

        if obj.base == money.currency:  # base -> other
            return Money(money.amount * obj.rate, obj.other)
        elif obj.other == money.currency:  # base <- other
            return Money(money.amount / obj.rate, obj.base)
        else:  # unknown currency
            raise TypeError(
                "Can't convert " + money.currency + " here (" + str(obj) + ")."
            )

    # operations

    def __mul__(obj, money):  # Money() * ExchangeRate() = convertedMoney
        """
        Convert Money between currencies using the multiplication operator.
        """
        if type(money) != Money:
            raise TypeError("Can't multiply ExchangeRates by anything but money.")

        return obj.convert(money)

    def __eq__(obj, other):
        """
        Check if two ExchangeRates are equal.
        """
        if type(obj) != type(other):
            return False

        if obj.rate == other.rate:  # equality
            return obj.base == other.base and obj.other == other.other
        elif obj.rate == 1 / other.rate:  # equality of the inverse
            return obj.base == other.other and obj.other == other.base

        return False

    def __hash__(obj):
        """
        Hash an ExchangeRate.
        """
        return hash((obj.rate, obj.base, obj.other))  # TODO same for inverse


# Exchanges are collections of ExchangeRates.


class Exchange:
    """
    Exchanges store multiple ExchangeRates and convert Money using them.
    """

    def __init__(obj, *exchangeRates):
        """
        Create an Exchange object.
        """
        obj.exchangeRates = []
        for exchangeRate in exchangeRates:
            if type(exchangeRate) == ExchangeRate:
                obj.insertExchangeRate(exchangeRate)
            elif type(exchangeRate) in [list, tuple]:
                obj.insertExchangeRate(*exchangeRate)
            else:
                raise TypeError("Unknow type for an exchangeRate.")

    def __repr__(obj):
        """
        Represent an Exchange.
        """
        if len(obj):
            return "{" + "; ".join([str(e) for e in obj.exchangeRates]) + "}"
        else:
            return "{ Empty Exchange }"

    def __len__(obj):
        """
        Get the stored amount of ExchangeRates.
        """
        return len(obj.exchangeRates)

    # checks

    def canConvert(obj, base, other=""):
        """
        Check for ways to convert money from one currency to another.
        """
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
        """
        Append the Exchange by another ExchangeRate (tuple, list or obj).
        """
        if len(args) == 1:  # rate
            newExchangeRate = args[0]
        elif len(args) == 3:  # base, other, rate
            newExchangeRate = ExchangeRate(args[0], args[1], args[2])
        else:
            raise ValueError("Invalid exchange rate for Exchange.insertExchangeRate().")

        existingRates = [exchangeRate for exchangeRate in obj.exchangeRates if newExchangeRate.getCurrencies() == exchangeRate.getCurrencies()]

        if existingRates == []:
            obj.exchangeRates += [newExchangeRate]
        else:
            oldExchangeRate = existingRates[0]
            if oldExchangeRate.base == newExchangeRate.base:
                oldExchangeRate.rate = newExchangeRate.rate
            else:
                oldExchangeRate.rate = 1 / newExchangeRate.rate

    # transform Money - unlimited steps of conversion possible :) - @finnmglas
    def exchangeRatePath(
        obj, currency, other, forwardPath=[], backwardPath=[], verbose=False
    ):
        """
        Find a path of ExchangeRates to convert one currency to another.
        """
        if verbose:
            print("Converters:", currency, "=>", other)
            print("\t", forwardPath, backwardPath)

        if currency == other:  # for 1, 2, 4, 6 conversions
            return forwardPath + backwardPath

        forwardOptions = [
            exchangeRate
            for exchangeRate in obj.exchangeRates
            if currency in exchangeRate.getCurrencies()
            and exchangeRate not in forwardPath
        ]
        backwardOptions = [
            exchangeRate
            for exchangeRate in obj.exchangeRates
            if other in exchangeRate.getCurrencies()
            and exchangeRate not in backwardPath
        ]

        if not len(forwardOptions) or not len(backwardOptions):
            raise ValueError(
                "Can't convert the currencies "
                + currency
                + " and "
                + other
                + " using this exchange."
            )

        if verbose:
            print(currency, "can be converted using", forwardOptions)
            print(other, "can be converted using", backwardOptions)

        common = [
            exchangeRate
            for exchangeRate in forwardOptions
            if exchangeRate in backwardOptions
        ]

        if common != []:  # for 3, 5, 7 conversions
            if verbose:
                print("Common conversions:", common)
            return forwardPath + [common[0]] + backwardPath

        if verbose:
            print("No Solution yet")

        possibleContinuations = [
            (forwardOption, backwardOption)
            for forwardOption in forwardOptions
            for backwardOption in backwardOptions
        ]
        for forwardOption, backwardOption in possibleContinuations:
            common = obj.exchangeRatePath(
                forwardOption.getOther(currency),
                backwardOption.getOther(other),
                forwardPath + [forwardOption],
                [backwardOption] + backwardPath,
                verbose,
            )
            return common

    def convert(obj, money, destinationCurrency, verbose=False):
        """
        Convert Money to a destination-currency.
        """
        if type(money) != Money:
            raise TypeError("Can't convert " + str(type(money)) + " to money.")

        if money.currency == destinationCurrency:
            return money
        # get conversions path
        conversions = obj.exchangeRatePath(
            money.currency, destinationCurrency, verbose=verbose
        )
        if verbose:
            print("ExchangePath:", conversions)
            print("Money:", money)

        convertedMoney = money
        # 'walk' the conversions path
        for exchangeRate in conversions:
            convertedMoney = exchangeRate.convert(convertedMoney)
            if verbose:
                print("Converted to:", convertedMoney)

        return convertedMoney
