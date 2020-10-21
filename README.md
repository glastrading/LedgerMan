
# LedgerMan :ledger:

Yet another python library for finance.

[![PyPI - Version][pypi-version-badge]][pypi]
[![Downloads][pepi-downloads-badge]][pepy tech]
[![Discord][discord-badge]][discord]
[![Code style: black][code-black-badge]][code-black]


<details>
  <summary>Table of contents</summary>

## Table of contents

+ [1 - Installation](#installation)
+ [2 - Usage](#usage)
  + [2.1 - Money](#usage-money)
  + [2.2 - Exchange Rates](#usage-exchange-rates)
  + [2.3 - Accounts](#usage-accounts)
+ [3 - Tools](#tools)
  + [3.1 - PyMoney Syntax Extender](#tools-pymoney)
    + [3.1.1 - PyMoney Syntax](#tools-pymoney-money)
+ [4 - Contributing](#contributing)
+ [5 - License (MIT)](#license)

</details>

<a id="installation"></a>
## 1 - Installation

To install LedgerMan, run `pip install ledgerman`.

<a id="usage"></a>
## 2 - Usage

Start by importing LedgerMan:

```python
from ledgerman import *
```

<a id="usage-money"></a>
### 2.1 - Let's talk Money

For finanial calculations, the `Money` class is very useful:

```python
m1 = Money() # default: 0 EUR
m2 = Money(10) # 10 EUR
m3 = Money(10, "USD")
```

You can interact with `Money` as you would expect:

```python
m = Money(20)

m += 5
m += Money(5)

m /= 2
m -= 5
m == 10 # true

if m:
  print("We're rich!") # will be printed

m - Money(20, "ETH") # ERROR - you can't add different currencies
```

... pretty straight forward!

<a id="usage-exchange-rates"></a>
### 2.2 - Exchange Rates

Whenever you want to work with multiple currencies, you may want to convert them:

```python
m = Money(20, "EUR")
e = ExchangeRate("EUR", "USD", 1.17) # from 2020-10-15

e # 1 EUR => 1.17 USD
e.inverse() # 1 USD => 0.85 EUR

e.convert(m) # 23.4 USD
e * m # 24 USD (shorter conversion function)
```

Just add common exchange rates so you can add money objects of different currencies:

```python
# Add exchange rate
Money.addExchangeRate("EUR", "ETH", 0.0031) # from 2020-10-15

Money.canConvert("EUR", "ETH") # Check: true

m = Money(5, "ETH")
m.to("EUR") # 1612.90 EUR

m = Money(5, "ETH") + Money(200, "EUR") # 5.62 ETH
```

You can also fetch exchange rates from [exchangeratesapi.io](https://exchangeratesapi.io):

```python
fetch_exchangeratesapi()

1 EUR + 1 CHF - 1 USD # 1.0857478268531873 EUR
```

Note that those values are provided by the European Central Bank (see [their data](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html)) and
updated only once per day.

<a id="usage-accounts"></a>
### 2.3 - Accounts

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

<a id="tools"></a>
## 3 - Tools

LedgerMan comes with commandline utilities that help you do financial calculations:

<a id="tools-pymoney"></a>
### 3.1 - PyMoney

The PyMoney tool simplifies financial calculus by extending pythons syntax.

It also provides a commandline interface for you, similar to the python interpreter
cli - run `pymoney` after [installing LedgerMan](#installation) to check it out!

<a id="tools-pymoney-money"></a>
#### 3.1.1 - The PyMoney Syntax

If you feel like regular syntax ([view usage](#usage-money)) is just unnecessary, you will love the PyMoney syntax:

```python
# regular syntax:
m = Money(5, "USD")

# PyMoney syntax:
m = 5 USD
```

To use this syntax you will write python code like you regularily would (you can use the `.py` or a `.pymoney` extension) - once it comes to executing your code, you run `pymoney [filename.py]` instead of `python [filename.py]`.

You can also convert money way easier:
```python
# We want to add those two... but how?
m1 = 5 USD
m2 = 2 EUR

# define a conversion rate:
EUR => 1.17 USD

m3 = m1 + m2 # 7.34 USD
```

It's incredibly simple and works with any currency (`EUR`, `BTC`, `ETH`, `CHF`, `USD`, ...). Feels very much like python - a little easier!


<a id="contributing"></a>
## 4 - Contributing

If you somehow can't help with the development (you're busy, whatever...), make sure to [star this repository][star],
as that helps other developers find the LedgerMan python module.

Just [fork] this repository, change something and submit a pull request!
They'll likely be merged and you'll definitely get some feedback.

Just make sure the code doesn't fail any tests and you formatted it with [the black codeformatter][code-black] (`pip install black`).
Run `black .` to format all the code, run `pip install -e .` for a linked development installation (automatically updates your changes).

Make sure that all tests execute properly by running `nosetests` in the projects `src/` directory.

Join our [discord] to discuss the module, features, bugs and use-cases.. give some feedback or just hang out!

<a id="license"></a>
## 5 - License

[MIT](https://choosealicense.com/licenses/mit/)

  [discord]: https://discord.com/invite/BsZXaur
  [discord-badge]: https://img.shields.io/badge/discord-join%20chat-000

  [pypi]: https://pypi.org/project/ledgerman/
  [pypi-version-badge]: https://img.shields.io/pypi/v/ledgerman?color=000

  [pepy tech]: https://pepy.tech/project/ledgerman
  [pepi-downloads-badge]: https://img.shields.io/badge/dynamic/json?style=flat&color=000&maxAge=10800&label=downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Fledgerman

  [code-black]: https://github.com/psf/black
  [code-black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg

  [joingh]: https://github.com/join
  [newissue]: https://github.com/finnmglas/ledgerman/issues/new/choose
  [fork]: https://github.com/finnmglas/ledgerman/fork
  [star]: https://github.com/finnmglas/ledgerman/stargazers
