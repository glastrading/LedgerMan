class Money:
    defaultCurrency = "EUR"

    class ConversionError(Exception):
        pass

    def __init__(self, amount=0, currency=defaultCurrency):
        self.amount = amount
        self.currency = currency

    # --- conversions

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
            if self.currency != other.currency:
                raise Money.ConversionError(
                    "Can't compare different currencies without conversion."
                )
            return self.amount == other.amount
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
            if self.currency != other.currency:
                raise Money.ConversionError(
                    "Can't compare different currencies without conversion."
                )
            return self.amount < other.amount
        else:
            raise TypeError(
                "Can't compare " + str(type(self)) + " and " + str(type(other)) + "."
            )

    def __le__(self, other):
        if type(other) in [int, float]:
            return self.amount <= other
        elif type(other) == type(self):
            if self.currency != other.currency:
                raise Money.ConversionError(
                    "Can't compare different currencies without conversion."
                )
            return self.amount <= other.amount
        else:
            raise TypeError(
                "Can't compare " + str(type(self)) + " and " + str(type(other)) + "."
            )

    def __gt__(self, other):
        if type(other) in [int, float]:
            return self.amount > other
        elif type(other) == type(self):
            if self.currency != other.currency:
                raise Money.ConversionError(
                    "Can't compare different currencies without conversion."
                )
            return self.amount > other.amount
        else:
            raise TypeError(
                "Can't compare " + str(type(self)) + " and " + str(type(other)) + "."
            )

    def __ge__(self, other):
        if type(other) in [int, float]:
            return self.amount >= other
        elif type(other) == type(self):
            if self.currency != other.currency:
                raise Money.ConversionError(
                    "Can't compare different currencies without conversion."
                )
            return self.amount >= other.amount
        else:
            raise TypeError(
                "Can't compare " + str(type(self)) + " and " + str(type(other)) + "."
            )

    # --- calculations

    def __add__(self, other):
        if type(other) in [int, float]:
            return Money(self.amount + other, self.currency)
        elif type(other) == type(self):
            if self.currency != other.currency:
                raise Money.ConversionError(
                    "Can't add different currencies without conversion."
                )
            return Money(self.amount + other.amount, self.currency)
        else:
            raise TypeError(
                "Can't add " + str(type(self)) + " and " + str(type(other)) + "."
            )

    def __sub__(self, other):
        if type(other) in [int, float]:
            return Money(self.amount - other, self.currency)
        elif type(other) == type(self):
            if self.currency != other.currency:
                raise Money.ConversionError(
                    "Can't subtract different currencies without conversion."
                )
            return Money(self.amount - other.amount, self.currency)
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
            return self.amount / other.amount
        else:
            raise TypeError(
                "Can't divide " + str(type(self)) + " by " + str(type(other)) + "."
            )

    def __mod__(self, other):
        if type(other) in [int, float]:
            return Money(self.amount % other, self.currency)
        elif type(other) == type(self):
            return self.amount % other.amount
        else:
            raise TypeError(
                "Can't mod " + str(type(self)) + " by " + str(type(other)) + "."
            )
