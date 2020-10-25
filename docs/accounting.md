
# Accounting

LedgerMan implements classes for you to use for accounting and analyzing accounts.

## Accounts

LedgerMan Accounts use [double-entry bookkeeping](https://en.wikipedia.org/wiki/Double-entry_bookkeeping):

Accounts types can be `DEBIT` or `CREDIT`, that simply means a `DEBIT` account increases on `debit()` and a `CREDIT` account on `credit()`.

```python
# create accounts
cash = Account(Account.Type.DEBIT)
loan = Account(Account.Type.CREDIT)

# we need 10K EUR from the bank
amount = Money("10000 EUR")

# debit the amount to cash (ASSET), credit it from loan (LIABILITY)
cash.debit(amount, loan)

cash.balance == Money("10000 EUR") # true
loan.balance == Money("10000 EUR") # true

# pay the loan off again
loan.debit("10000 EUR")
```

Debit accounts and credit accounts should always equal to 0.
By default, they will, unless someone does an error.

You can also name Accounts and annotate transactions:

```python
cash = Account(Account.Type.DEBIT, name="My Wallet")
loan = Account(Account.Type.CREDIT, name="My Loan")

amount = Money("10000 EUR")
cash.debit(amount, loan, note="Take the loan from my bank.")
loan.debit(amount, cash, note="Pay back what I owe the bank.")
```
