# LedgerMan CLI tools

LedgerMan implements **commandline utilities** that will help you do financial calculations.

After installing LedgerMan, you will be able to run the `ledgerman` command. Its general syntax is `legdgerman [tool] (arguments)`, while some tools have an alias command that abbreviates the syntax to `[tool] (arguments)`.

The following sections discuss the specific **tools provided by LedgerMan**:

| | helps you with | command | alias |
|-|-|-|-|
| [**LedgerMan Convert**](#tools-convert) | Quick currency conversions from the commandline. | `ledgerman convert` | - |
| [**LedgerMan GUI**](#tools-gui) | A graphical user-interface for LedgerMan | `ledgerman gui` | - |
| | ***More tools coming soon!*** | | |

<a id="tools-convert"></a>
## LedgerMan Convert

LedgerMan Convert is a tool to convert between currencies. It fetches currencies from all available APIs and uses those for conversions.

| use case | syntax | example |
|-|-|-|
| Get an exchange rate: | `ledgerman convert [src] [dest]` | `ledgerman convert EUR BTC` |
| Fetch and print all available exchange rates: | `ledgerman convert --rates` | - |
| Learn more or get help: | `ledgerman convert -h` | - |

<a id="tools-gui"></a>
## LedgerMan GUI

The LedgerMan Graphical User Interface is a program that you can start by running `ledgerman gui`.
