from .exchange_rate import ExchangeRate
from .money import Money


class Exchange:

    """
    Exchanges are collections of ExchangeRates.
    They enable multiple-step conversions between currencies.
    """

    def __init__(self, *exchangeRates):

        """
        Create an exchange.
        """

        self.exchangeRates = []
        for exchangeRate in exchangeRates:
            if isinstance(exchangeRate, ExchangeRate):
                self.insertExchangeRate(exchangeRate)
            elif type(exchangeRate) in [list, tuple]:
                self.insertExchangeRate(*exchangeRate)
            else:
                raise TypeError(
                    "Unknown type for an exchangeRate: '"
                    + type(exchangRate).__name__
                    + "'."
                )

    def __len__(self):

        """
        Get the stored amount of Exchange Rates.
        """

        return len(self.exchangeRates)

    def insertExchangeRate(self, *args):  # update / append a rate

        """
        Add a new or update an existing ExchangeRate.
        """

        if len(args) == 1:  # exchangeRate
            newExchangeRate = args[0]
        elif len(args) == 3:  # baseCurrency, destCurrency, rate
            newExchangeRate = ExchangeRate(args[0], args[1], args[2])
        else:
            raise ValueError("Invalid exchange rate for Exchange.insertExchangeRate().")

        existingRates = [
            exchangeRate
            for exchangeRate in self.exchangeRates
            if newExchangeRate.getCurrencies() == exchangeRate.getCurrencies()
        ]

        if existingRates == []:
            self.exchangeRates += [newExchangeRate]
        else:
            oldExchangeRate = existingRates[0]  # expecting len(existingRates) == 1
            if oldExchangeRate.baseCurrency == newExchangeRate.baseCurrency:
                oldExchangeRate.rate = newExchangeRate.rate
            else:
                oldExchangeRate.rate = 1 / newExchangeRate.rate

    def getCurrencies(self):

        """
        Get a list of all supported currencies.
        Having two currencies included here does not mean they can be converted.
        """

        return {e.baseCurrency for e in self.exchangeRates} + {
            e.destCurrency for e in self.exchangeRates
        }

    def canConvert(self, baseCurrency, destCurrency=None):
        if destCurrency == None:
            return baseCurrency in self.getCurrencies()
        else:
            return len(self.exchangeRatePath(baseCurrency, destCurrency)) > 0

    # transform Money - unlimited steps of conversion possible :) - @finnmglas
    def exchangeRatePath(
        self, baseCurrency, destCurrency, forwardPath=[], backwardPath=[], verbose=False
    ):

        """
        Find a path of ExchangeRates to convert one currency to another.
        """

        if verbose:
            print("Converters:", baseCurrency, "=>", destCurrency)
            print("\t", forwardPath, backwardPath)

        if baseCurrency == destCurrency:  # for 1, 2, 4, 6 conversions
            return forwardPath + backwardPath

        forwardOptions = [
            exchangeRate
            for exchangeRate in self.exchangeRates
            if baseCurrency in exchangeRate.getCurrencies()
            and exchangeRate not in forwardPath
        ]
        backwardOptions = [
            exchangeRate
            for exchangeRate in self.exchangeRates
            if destCurrency in exchangeRate.getCurrencies()
            and exchangeRate not in backwardPath
        ]

        if not len(forwardOptions) or not len(backwardOptions):
            return []

        if verbose:
            print(baseCurrency, "can be converted using", forwardOptions)
            print(destCurrency, "can be converted using", backwardOptions)

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
            common = self.exchangeRatePath(
                forwardOption.getDest(baseCurrency),
                backwardOption.getDest(destCurrency),
                forwardPath + [forwardOption],
                [backwardOption] + backwardPath,
                verbose,
            )
            return common

    def convert(self, money, destCurrency, verbose=False):

        """
        Convert Money to a destination-currency.
        """

        if not isinstance(money, Money):
            raise TypeError("Can't convert " + str(type(money)) + " to money.")

        if money.currency == destCurrency:
            return money

        # get conversions path
        conversions = self.exchangeRatePath(
            money.currency, destCurrency, verbose=verbose
        )

        if conversions == []:
            raise ValueError(
                "Can't convert the currencies "
                + money.currency
                + " and "
                + destCurrency
                + " using this exchange."
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
