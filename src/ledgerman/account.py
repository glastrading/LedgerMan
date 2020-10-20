from .money import Money
from .exchange import ExchangeRate

import time


class Account:
    """
    The Account class stores and tracks Money.
    """

    def __init__(obj, name="Account", balance=Money(0), record=None):
        """
        Create an Account object.
        """
        obj.name = name
        if type(balance) in [int, float]:  # balance -> amount
            balance = Money(balance)
        elif type(balance) == str:  # balance -> currency
            balance = Money(0, balance)
        obj.balance = balance
        if record == None:  # record is of type Record()
            record = Record()
        obj.record = record

    def __repr__(obj):
        """
        Represent an Account.
        """
        return obj.name + ": " + str(obj.balance)

    # operations
    def __add__(obj, other):
        """
        Add Money to an Account.
        """
        acc = Account(obj.name, -obj.balance, obj.record.copy())
        if type(other) == type(obj):  # account + account
            acc.balance += other.balance
            acc.record.append(Transaction(other.balance))
        else:  # account + money, account + int
            acc.balance += other
            acc.record.append(Transaction(other))
        return acc

    def __sub__(obj, other):
        """
        Subtract Money from an Account.
        """
        return obj + (-other)

    def __neg__(obj):
        """
        Negate an accounts Balance.
        """
        acc = Account(obj.name, -obj.balance, obj.record.copy())
        acc.record.append(Transaction(-obj.balance * 2, "Negate balance"))
        return acc

    def __mul__(obj, other):
        """
        Multiply an Accounts balance by a number.
        """
        acc = Account(obj.name, obj.balance, obj.record.copy())
        acc.balance *= other
        acc.record.append(
            Transaction(acc.balance - obj.balance, "Multiply by " + str(other))
        )
        return acc

    def __truediv__(obj, other):
        """
        Divide an Accounts balance by a number.
        """
        return obj * (1 / other)


class Record:
    """
    A record stores transactions.
    """

    def __init__(obj, transactions=[]):
        """
        Create a record.
        """
        obj.transactions = transactions

    def __len__(obj):
        """
        Get the length of the record.
        """
        return len(obj.transactions)

    def copy(obj):
        """
        Copy the record.
        """
        return Record(obj.transactions.copy())

    def __repr__(obj):
        """
        Display the stored transactions.
        """
        recordRepresentation = "----- Record -----\n"
        for transaction in obj.transactions:
            recordRepresentation += str(transaction) + "\n"
        if len(obj) == 0:
            recordRepresentation += "No transactions.\n"
        return recordRepresentation

    def append(obj, transaction):
        """
        Append the transaction record.
        """
        obj.transactions += [transaction]

    def __add__(obj, other):
        """
        Append the transaction record (addition operator).
        """
        obj.append(other)


class Transaction:
    """
    Transactions are records of a money transfer at some time.
    """

    def __init__(obj, valueChange, description=None, timeStamp=None):
        """
        Create a Transaction object.
        """
        obj.valueChange = valueChange
        if description:
            obj.description = description
        if timeStamp == None:
            timeStamp = int(time.time())
        obj.time = timeStamp

    def __repr__(obj):
        """
        Represent a Transaction.
        """
        return "[" + str(obj.time) + "] Transaction: " + str(obj.valueChange)
