import decimal
from jcdb import Object


class Decimal(Object):

    """
    LedgerMan's type for storing numbers with high precision.
    """

    def __init__(self, argument="0", precision=8):
        self.precision = precision
        decimal.getcontext().prec = self.getPrecision()

        if type(argument) != decimal.Decimal:
            argument = decimal.Decimal(argument)

        self.value = "{:f}".format(argument.normalize() * decimal.Decimal(1))

    def n(self):
        decimal.getcontext().prec = self.getPrecision()
        return decimal.Decimal(self.value)

    def getPrecision(self):
        return self.precision + 1  # offset somehow needed to keep things working

    def smallest(self):
        decimal.getcontext().prec = self.getPrecision()
        return decimal.Decimal("0." + self.getPrecision() * "0" + "1")

    ## --- Datamodel operations --- ##

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    def __eq__(self, other):
        if type(other) != Decimal:
            other = Decimal(other)

        decimal.getcontext().prec = self.getPrecision()
        return self.n() == other.n()

    def __gt__(self, other):
        if type(other) != Decimal:
            other = Decimal(other)

        decimal.getcontext().prec = self.getPrecision()
        return self.n() > other.n()

    def __ge__(self, other):
        if type(other) != Decimal:
            other = Decimal(other)

        decimal.getcontext().prec = self.getPrecision()
        return self.n() >= other.n()

    def __lt__(self, other):
        if type(other) != Decimal:
            other = Decimal(other)

        decimal.getcontext().prec = self.getPrecision()
        return self.n() < other.n()

    def __le__(self, other):
        if type(other) != Decimal:
            other = Decimal(other)

        decimal.getcontext().prec = self.getPrecision()
        return self.n() <= other.n()

    def __add__(self, other):
        if type(other) != Decimal:
            other = Decimal(other)

        decimal.getcontext().prec = self.getPrecision()
        return Decimal(self.n() + other.n(), self.precision)

    def __sub__(self, other):
        if type(other) != Decimal:
            other = Decimal(other)

        decimal.getcontext().prec = self.getPrecision()
        return Decimal(self.n() - other.n(), self.precision)

    def __mul__(self, other):
        if type(other) != Decimal:
            other = Decimal(other)

        decimal.getcontext().prec = self.getPrecision()
        return Decimal(self.n() * other.n(), self.precision)

    def __truediv__(self, other):
        if type(other) != Decimal:
            other = Decimal(other)

        decimal.getcontext().prec = self.getPrecision()
        return Decimal(self.n() / other.n(), self.precision)

    def __abs__(self):
        return Decimal(abs(self.n()))

    def __neg__(self):
        return Decimal(0) - self


Object.register(Decimal)
