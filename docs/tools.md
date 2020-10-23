# LedgerMan CLI tools

LedgerMan implements **commandline utilities** that will help you do financial calculations.

After installing LedgerMan, you will be able to run the `ledgerman` command. Its general syntax is `legdgerman [tool] (arguments)`, while some tools have an alias command that abbreviates the syntax to `[tool] (arguments)`.

The following sections discuss the specific **tools provided by LedgerMan**:

+ [**LedgerMan Convert**](#tools-convert) - Quick currency conversions from the commandline. - `ledgerman convert`
+ [**PyMoney Syntax Extension**](#tools-pymoney) - Runs `.pymoney` type files in which you can use LedgerMan types with more comprehensive syntax (like `money = 1 EUR`) - `ledgerman run` (alias `pymoney`).
+ ***More tools coming soon!***

<a id="tools-convert"></a>
## LedgerMan Convert

LedgerMan Convert is a tool to convert between currencies. It fetches currencies from all available APIs and uses those for conversions.

**Get an exchange rate:**

`ledgerman convert [src] [dest]` -> `ledgerman convert EUR BTC`

**Fetch and print all available exchange rates:**

`ledgerman convert --rates`

**Convert to a specific currency:**

`ledgerman convert [expression] [dest]` -> `ledgerman convert "2.2 BTC" USD`

**Add / subtract multiple currencies through automatic conversion:**

`ledgerman convert [expression]` -> `ledgerman convert "1 BTC + 200 EUR"`

**Learn more or get help:** `ledgerman convert -h`

## PyMoney syntax extension

> Finance is complex enough, why bother with complex syntax?

The PyMoney tool simplifies financial calculus by extending Pythons syntax to what we call the [PyMoney syntax](#tools-pymoney-syntax). It can be interpreted using the `ledgerman run` or the `pymoney` command.

<a id="tools-pymoney-syntax"></a>
### The PyMoney Syntax

If you feel like regular syntax is just unnecessary complex, you will love the PyMoney syntax:

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
