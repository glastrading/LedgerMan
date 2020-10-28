# Finances

LedgerMan implements some core classes that help you interact with finances.

## Money

For finanial calculations, the `Money` class is very useful:

```python
m1 = Money() # default: 0 EUR
m2 = Money("10 USD")
```

You can set a precision (how many digits are stored) for money objects:

```python
m3 = Money("10 BTC", roundTo="0.00000001")
```

Do basic calculations with `Money`:

```python
m = Money("20 EUR")

m += Money("5 EUR")
m += Money("5 EUR")

m /= 2
m -= Money("5 EUR")
m == Money("10 EUR") # true

m - Money("20 ETH") # ERROR - you can't add different currencies
```

## Exchange Rates

### Exchanging Money

Whenever you want to work with multiple currencies, you likely want to convert them:

```python
m = Money("20 EUR")
e = ExchangeRate("EUR", "USD", 1.17) # from 2020-10-15

e.convert(m) # 23.4 USD
```

Just add common exchange rates so you can add money objects of different currencies:

```python
# Add exchange rate
Money.insertExchangeRate("EUR", "ETH", 0.0031) # from 2020-10-15

Money.canConvert("EUR", "ETH") # Check: true

m = Money("5 ETH")
m.to("EUR") # 1612.90 EUR

m = Money("5 ETH") + Money("200 EUR") # 5.62 ETH
```

The more exchange rates with already known conversions you add, the more conversions you can perform:

```python
Money.insertExchangeRate("EUR", "ETH", 0.0031) # from 2020-10-15
Money.insertExchangeRate("EUR", "USD", 1.17) # from 2020-10-15

Money.canConvert("EUR", "USD") # true; Both exchangeRates are used.

m = Money("5 ETH")
m.to("USD")

m = Money("5 ETH") + Money("200 USD")
```

## Exchange-Rate APIs

You can fetch exchange rates from the following APIs:

| api | assets | refresh-rates |
|-|-|-|
| [ECB](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html) (European Central Bank) | Common currencies - `USD`, `JPY`, `BGN`, `CZK`, `DKK`, `GBP`, `HUF`, `PLN`, `RON`, `SEK`, `CHF`, `ISK`, `NOK`, `HRK`, `RUB`, `TRY`, `AUD`, `BRL`, `CAD`, `CNY`, `HKD`, `IDR`, `ILS`, `INR`, `KRW`, `MXN`, `MYR`, `NZD`, `PHP`, `SGD`, `THB`, `ZAR` | daily around 16:30 |
| [Bitpanda](https://www.bitpanda.com/en) | Crypto - `BTC`, `BCI5`, `BEST`, `PAN`, `BCI10`, `BCI25`, `XAU`, `ETH`, `LINK`, `USDT`, `MIOTA`, `XRP`, `ADA`, `TRX`, `VET`, `OMG`, `NEO`, `QTUM`, `LTC`, `XEM`, `XTZ`, `XAG`, `YFI`, `CHZ`, `XLM`, `ONT`, `BCH`, `USDC`, `EOS`, `UNI`, `WAVES`, `ATOM`, `DOT`, `SNX`, `DASH`, `ZRX`, `BAT`, `KMD`, `ETC`, `DOGE`, `ZEC`, `XPD`, `REP`, `LSK`, `COMP`, `XPT`, `MKR`, `FIL`, `BAND`, `KNC`, `AAVE`, `UMA`, `REN` | A few times per second |
| [CoinGecko](https://www.coingecko.com/en) | Common crypto - `eth`, `btc`, `ltc`, `trx`, `usdt`, `xrp`, `link`, `best`, `pan`, `miota`, `ada`, `vet`, `omg`, `neo`, `qtum`, `xem`, `xtz`, `yfi`, `chz`, `xlm`, `ont`, `bch`, `usdc`, `eos`, `uni`, `waves`, `atom`, `dot`, `snx`, `dash`, `zrx`, `bat`, `kmd`, `etc`, `doge`, `zec`, `rep`, `lsk`, `comp`, `mkr` | every few seconds |

Fetch rates from an API and just use the fetched conversions implicitly when doing money operations (`+ - * /`):

**The European central Bank:**

```python
# default: European Central Bank
Money.fetchRates()

# will print all fetched rates (here: ecb)
Money.fetchRates(verbose=True)

# fetch from the European Central Bank (equal)
Money.fetchRates("ecb")

m = Money("5 EUR") + Money("5 USD") + Money("5 CHF") # no error
```

**Bitpanda:**

```python
# fetch crypto from Bitpanda
Money.fetchRates("bitpanda")

m = Money("5 EUR") + Money("5 ETH") + Money("5 LTC") # no error
```

**CoinGecko:**

```python
# fetch crypto from CoinGecko
Money.fetchRates("coingecko")

m = Money("5 EUR") + Money("5 ETH") + Money("5 LTC") # no error
```

Note that the APIs may not be reliable all the time and that you will need a network connection.
