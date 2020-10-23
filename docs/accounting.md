# Accounting

LedgerMan will also provide useful accounting models that will help you calculate
basic financial statements for everything from Trading-Accounts to corporations.

## Accounts

Likely you want to keep track of when - and why you spend your money, that is what Accounts do:

```python
# Get yourself an account
a = Account("MyBankAccount", "USD")

# Check your balance
a.balance # 0 USD

# Put some money in there
a += Money(50, "USD")

# Buy some icecream
a -= Money(2.50, "USD")

# check the transaction record
a.record.show()
```

_More is coming soon!_
