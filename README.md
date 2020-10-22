
# LedgerMan :ledger:

> Yet another python library for finance. ***Why?***

+ LedgerMan is **comprehensive**. Check out [its usage](#usage)!
+ LedgerMan is **open, welcoming and transparent**: [join us on discord][discord]!
+ LedgerMan provides **powerful** financial tools and models.

[![PyPI - Version][pypi-version-badge]][pypi]
[![Downloads][pepi-downloads-badge]][pepy tech]
[![Discord][discord-badge]][discord]
[![Code style: black][code-black-badge]][code-black]

<a id="contents"></a>
<details>
  <summary>Overview</summary>

## Table of contents

+ [1 - Installation](#installation) :arrow_down:
+ [2 - Using the Library](#usage)
  + [2.1 - Money](#usage-money) :heavy_dollar_sign:
  + [2.2 - Exchange Rates](#usage-exchange-rates) :currency_exchange:
    + [2.2.1 - How to exchange](#usage-exchange-howto)
    + [2.2.2 - Fetching exchange-rates from APIs](#usage-exchange-api) :arrows_clockwise:
  + [2.3 - Accounts](#usage-accounts) :bank:
+ [3 - LedgerMan Tools](#tools) :toolbox:
  + [3.1 - LedgerMan to convert currencies](#tools-convert)
  + [3.2 - PyMoney Syntax Extender](#tools-pymoney)
    + [3.2.1 - The PyMoney Syntax](#tools-pymoney-syntax)
    + [3.2.1 - Running PyMoney](#tools-pymoney-run)
+ [4 - Contributing](#contributing) :octocat:
+ [5 - License:](#license) [MIT]

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

_<sub>[`back to overview`][contents]</sub>_
<a id="usage-money"></a>
### 2.1 - Let's talk Money :heavy_dollar_sign:

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

_<sub>[`back to overview`][contents]</sub>_
<a id="usage-exchange-rates"></a>
### 2.2 - Exchange Rates :currency_exchange:

<a id="usage-exchange-howto"></a>
#### 2.2.1 - Exchanging Money

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

The more exchange rates you add, the more conversions you can perform - LedgerMan
also supports **implicit conversions through any level of exchange rates**. This
means that by defining a `BTC` to `EUR` and a `EUR` to `USD` ExchangeRate, you
will be able to add `BTC` and `USD` objects and convert them on the fly too!

_<sub>[`back to overview`][contents]</sub>_
<a id="usage-exchange-api"></a>
#### 2.2.2 - Fetching Exchange-Rates from an API :arrows_clockwise:

You can fetch exchange rates from the following APIs:

| api | assets | refresh-rates |
|-|-|-|
| [ECB](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html) (European Central Bank) | Common currencies - `USD`, `JPY`, `BGN`, `CZK`, `DKK`, `GBP`, `HUF`, `PLN`, `RON`, `SEK`, `CHF`, `ISK`, `NOK`, `HRK`, `RUB`, `TRY`, `AUD`, `BRL`, `CAD`, `CNY`, `HKD`, `IDR`, `ILS`, `INR`, `KRW`, `MXN`, `MYR`, `NZD`, `PHP`, `SGD`, `THB`, `ZAR` | daily around 16:30 |
| [CoinGecko](https://www.coingecko.com/en) | Common crypto - `eth`, `btc`, `ltc`, `trx`, `usdt`, `xrp`, `link`, `best`, `pan`, `miota`, `ada`, `vet`, `omg`, `neo`, `qtum`, `xem`, `xtz`, `yfi`, `chz`, `xlm`, `ont`, `bch`, `usdc`, `eos`, `uni`, `waves`, `atom`, `dot`, `snx`, `dash`, `zrx`, `bat`, `kmd`, `etc`, `doge`, `zec`, `rep`, `lsk`, `comp`, `mkr` | every few seconds |

Fetch rates from an API and just use the fetched conversions implicitly when doing money operations (`+ - * /`):

```python
# default: European Central Bank
Money.fetchRates()

# fetch from the European Central Bank
Money.fetchRates("ecb")

m = Money(5, "EUR") + Money(5, "USD") + Money(5, "CHF") # no error

# fetch crypto from CoinGecko
Money.fetchRates("coingecko")

m = Money(5, "EUR") + Money(2, "ETH") + Money(10, "LTC") # no error

# will print all fetched rates (ecb)
Money.fetchRates(verbose=True)
```

Note that the APIs may not be reliable all the time and that you will need a network connection.

_<sub>[`back to overview`][contents]</sub>_
<a id="usage-accounts"></a>
### 2.3 - Accounts :bank:

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

_<sub>[`back to overview`][contents]</sub>_
<a id="tools"></a>
## 3 - LedgerMan Tools :toolbox:

LedgerMan implements **commandline utilities** that will help you do financial calculations.

After [installing LedgerMan](#installation), you will be able to run the `ledgerman` command. Its general syntax is `legdgerman [tool] (arguments)`, while some tools have an alias command that abbreviates the syntax to `[tool] (arguments)`.

The following sections discuss the specific **tools provided by LedgerMan**:

| :wrench: | helps you with | command | alias |
|-|-|-|-|
| [**LedgerMan Convert**](#tools-convert) | Quick currency conversions from the commandline. | `ledgerman convert` | - |
| [**PyMoney Syntax Extension**](#tools-pymoney) | Runs `.pymoney` type files in which you can use LedgerMan types with more comprehensive syntax (like `money = 1 EUR`). | `ledgerman run` | `pymoney` |
| :wrench: | ***More tools coming soon!*** | :wrench: | :wrench: |

_<sub>[`back to overview`][contents]</sub>_
<a id="tools-convert"></a>
### 3.1 - LedgerMan Convert

LedgerMan Convert is a tool to convert between currencies. It fetches currencies from all [available APIs](#usage-exchange-api) and uses those for conversions.

| use case | syntax | example |
|-|-|-|
| Get an exchange rate: | `ledgerman convert [src] [dest]` | `ledgerman convert EUR BTC` |
| Fetch and print all available exchange rates: | `ledgerman convert --rates` | - |
| Convert to a specific currency: | `ledgerman convert [expression] [dest]` | `ledgerman convert "2.2 BTC" USD` |
| Add / subtract multiple currencies through automatic conversion (result will be in the first used currency): | `ledgerman convert [expression]` | `ledgerman convert "1 BTC + 200 EUR"` |
| Learn more or get help: | `ledgerman convert -h` | - |

_<sub>[`back to overview`][contents] or [`view all tools`](#tools)</sub>_
<a id="tools-pymoney"></a>
### 3.2 - PyMoney syntax extension

> Finance is complex enough, why bother with complex syntax?

The PyMoney tool simplifies financial calculus by extending Pythons syntax to what we call the [PyMoney syntax](#tools-pymoney-syntax). It can be interpreted using the `ledgerman run` or the `pymoney` command.

<a id="tools-pymoney-syntax"></a>
#### 3.2.1 - The PyMoney Syntax

If you feel like regular syntax ([view usage](#usage-money)) is just unnecessary complex, you will love the PyMoney syntax:

```python
# regular syntax:
m = Money(5, "USD")

# PyMoney syntax:
m = 5 USD
```

You can also convert money between currencies way easier:
```python
# We want to add those two... but how?
m1 = 5 USD
m2 = 2 EUR

# define a conversion rate:
EUR => 1.17 USD

m3 = m1 + m2 # 7.34 USD
```

It's incredibly simple and works with any currency (`EUR`, `BTC`, `ETH`, `CHF`, `USD`, ...). Feels very much like python - less complex.

<a id="tools-pymoney-run"></a>
#### 3.2.2 - Running PyMoney code and files

To use the PyMoney syntax you will write python code like you regularily would. You can use the `.py` or a `.pymoney` extension, or whatever else you like.

Once it comes to executing your code, you'll use `ledgerman run [filename]` or the shorter alias `pymoney [filename]`.

It also provides an **interactive commandline shell** for you, similar to the Python Interpreter Shell - run `ledgerman run` or its alias `pymoney` without specifying a file.

_<sub>[`back to overview`][contents] or [`view all tools`](#tools)</sub>_
<a id="contributing"></a>
## 4 - Contributing :octocat:

If you somehow can't help with the development (you're busy, whatever...), make sure to [star this repository][star],
as that helps other developers find the LedgerMan python module.

Just [fork] this repository, change something and submit a pull request!
They'll likely be merged and you'll definitely get some feedback.

Just make sure the code doesn't fail any tests and you formatted it with [the black codeformatter][code-black] (`pip install black`).
Run `black .` to format all the code, run `pip install -e .` for a linked development installation (automatically updates your changes).

Make sure that all tests execute properly by running `nosetests` in the projects `src/` directory.

Join our [discord] to discuss the module, features, bugs and use-cases.. give some feedback or just hang out!

_<sub>[`back to overview`][contents], [`contact Finn`][contact] or [`sponsor this project ❤️`][sponsor]</sub>_
<a id="license"></a>
## 5 - License

[MIT License. Copyright 2020 Finn M Glas.][MIT]

_<sub>[`back to overview`][contents], [`contact Finn`][contact] or [`sponsor this project ❤️`][sponsor]</sub>_

<!-- Navigation -->
  [contents]: #contents

<!-- Finns owned media -->
  [contact]: https://contact.finnmglas.com
  [sponsor]: https://sponsor.finnmglas.com

<!-- Community -->
  [discord]: https://discord.com/invite/BsZXaur
  [discord-badge]: https://img.shields.io/badge/discord-join%20chat-000

<!-- GitHub related -->

  [joingh]: https://github.com/join
  [newissue]: https://github.com/finnmglas/ledgerman/issues/new/choose
  [fork]: https://github.com/finnmglas/ledgerman/fork
  [star]: https://github.com/finnmglas/ledgerman/stargazers

<!-- Python Package -->
  [pypi]: https://pypi.org/project/ledgerman/
  [pypi-version-badge]: https://img.shields.io/pypi/v/ledgerman?color=000

  [pepy tech]: https://pepy.tech/project/ledgerman
  [pepi-downloads-badge]: https://img.shields.io/badge/dynamic/json?style=flat&color=000&maxAge=10800&label=downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Fledgerman

  [code-black]: https://github.com/psf/black
  [code-black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg

<!-- Legal -->
  [MIT]: https://choosealicense.com/licenses/mit/
