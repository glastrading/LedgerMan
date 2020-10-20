
# LedgerMan :ledger:

Yet another python module for finance.

[![PyPI - Version][pypi-version-badge]][pypi]
[![Downloads][pepi-downloads-badge]][pepy tech]
[![Discord][discord-badge]][discord]
[![Code style: black][code-black-badge]][code-black]

## Installation

To install LedgerMan, run `pip install ledgerman`.

## Usage

Start by importing LedgerMan:

```python
from ledgerman import *
```

### Let's talk Money

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
m -=
m == 15 # true

if m:
  print("We're rich!") # will be printed

m - Money(20, "ETH") # ERROR - you can't add different currencies
```

... pretty straight forward!

### Exchange Rates

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

## Contributing

If you somehow can't help with the development (you're busy, whatever...), make sure to [star this repository][star],
as that helps other developers find the LedgerMan python module.

Just [fork] this repository, change something and submit a pull request!
They'll likely be merged and you'll definitely get some feedback.

Just make sure the code doesn't fail any tests and you formatted it with [the black codeformatter][code-black] (`pip install black`).
Run `black .` to format all the code, run `pip install -e .` for a linked development installation (automatically updates your changes).

Make sure that all tests execute properly by running `nosetests` in the projects `src/` directory.

Join our [discord] to discuss the module, features, bugs and use-cases.. give some feedback or just hang out!

## License

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
