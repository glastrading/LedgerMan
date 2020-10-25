# Basic finances

LedgerMan implements some base classes to help you interact with finances.

## Money

For finanial calculations, the `Money` class is very useful:

```python
m1 = Money() # default: 0 EUR
m2 = Money(10) # 10 EUR
m3 = Money(10, "USD")
```

You can interact with `Money` as you likely would expect:

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

### Exchange Rates

### Exchanging Money

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

### Fetching Exchange-Rates from an API

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
