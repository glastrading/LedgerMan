
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
loan.debit("10000 EUR", cash)
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

To model an action that happened in the past or may happen in the future, you can add a date parameter to transactions on your accounts:

```python
cash.debit(amount, loan, date="2020-01-05 10:00:00")
```

## Journals

Accounts have associated journals that keep track of the accounts balance over time, transactions and notes.

You can print journals to see their entries. This is the journal for our example above where we took a 10k loan and payed it back. As we didn't specify any dates, it looks like we look the loan and payed it back in the same second:

```
[
    {
        "amount": "10000.0000 EUR",
        "credit": "My Loan (credit)",
        "date": "2020-10-25 08:31:20",
        "debit": "My Wallet (debit)",
        "note": "Take the loan from my bank.",
        "result": "10000.0000 EUR",
        "type": "debit"
    },
    {
        "amount": "10000.0000 EUR",
        "credit": "My Wallet (debit)",
        "date": "2020-10-25 08:31:20",
        "debit": "My Loan (credit)",
        "note": "Pay back what I owe the bank.",
        "result": "0.0000 EUR",
        "type": "credit"
    }
]
```

## Currency Trades

Trades can be used to model currency-pair-trades:

```python
# Get Exchange Rates
Money.fetchRates("coingecko")

# Create a Trade
myEthereum = Trade("EUR", "ETH")

# Trade some
myEthereum.trade("100 EUR", "0.4514155 ETH", "2020-06-08 20:02:00")

# Check Profits
myEthereum.getProfits()

# Display details
print(myEthereum)
```

## Trade Accounts

If you trade more than one pair of currencies (you for example buy `BTC` and `ETH` from `EUR`), you can use a TradeAccount. It internally creates instances of the `Trade` class:

```python
# Get Exchange Rates
Money.fetchRates("coingecko")

acc = TradeAccount()

acc.trade("340 EUR", "1 ETH")
acc.trade("10000 EUR", "1 BTC")

print("Expense:", acc.getExpense())
print("Balance:", acc.getBalance())
print("Profits:", acc.getProfits())
```
