import decimal


class Money:

    """
    Money.
    """

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

    def __repr__(money):

        """
        Represent a Money object: '[amount] [currency]'.
        """

        return (
            str(
                money.amount.quantize(
                    decimal.Decimal(money.roundTo), rounding=decimal.ROUND_HALF_EVEN
                )
            )
            + " "
            + money.currency
        )

    def to(money, currency):

        """
        Convert Money to a currency.
        """

        if money.currency == currency:
            return money
        else:
            raise ValueError("can't convert '" + str(money) + "' to '" + currency + "'")

    # operations

    def __eq__(money, other):

        """
        Check equality of Money objects.
        """

        if not isinstance(other, Money):
            raise TypeError(
                "unsupported operand type(s) for ==: 'Money' and '"
                + type(other).__name__
                + "'"
            )

        return other.to(money.currency).amount == money.amount

    def __add__(money, other):

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
            str(money.amount + other.to(money.currency).amount) + " " + money.currency
        )

    def __sub__(money, other):

        """
        Subtract Money objects.
        """

        if not isinstance(other, Money):
            raise TypeError(
                "unsupported operand type(s) for -: 'Money' and '"
                + type(other).__name__
                + "'"
            )

        return Money(
            str(money.amount - other.to(money.currency).amount) + " " + money.currency
        )

    def __neg__(money):

        """
        Negate Money objects.
        """

        return Money() - money

    def __mul__(money, other):

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
                decimal.Decimal(money.roundTo), rounding=decimal.ROUND_HALF_EVEN
            )

        return Money(str(money.amount * other) + " " + money.currency)

    def __truediv__(money, other):

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
            return money.amount / other.to(money.currency).amount

        return Money(str(money.amount / other) + " " + money.currency)


decimal.getcontext().prec = 128  # general max precision
