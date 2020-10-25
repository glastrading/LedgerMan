[![PyPI - Version][pypi-version-badge]][pypi]
[![Downloads][pepi-downloads-badge]][pepy tech]
[![Discord][discord-badge]][discord]
[![Code style: black][code-black-badge]][code-black]

# LedgerMan :ledger:

> Yet another python library for finance. ***Why?***

+ LedgerMan is **comprehensive**.
+ LedgerMan is **open and transparent**.
+ LedgerMan provides **powerful** financial tools and models.

<a id="installation"></a>
## Installation

To install LedgerMan, run `pip install ledgerman`.

<a id="usage"></a>
## Usage

Start by importing LedgerMan:

```python
from ledgerman import *
```

Example - convert EUR to USD:

```python
Money.fetchRates() # from the European Central Bank

m = Money(10, "EUR")
print(m.to("USD")) # convert currencies
```

Check out our [**documentation**](https://ledgerman.readthedocs.io) to learn more.

<a id="contributing"></a>
## Contributing :octocat:

If you can't help with the development (you're busy, whatever...), make sure to ***star this repository***, as that helps other developers find LedgerMan:

[![][shield-star]][star]

You can also join our [discord]!

<a id="contributing-code"></a>
### Contributing Code

+ **Fork** this repository:
<br><p style="margin-left:30px;">[![][shield-fork]][fork]</p>
+ **Set up** the environment:<p>Run `pip install -e .` in LedgerMan's `src/` for a development installation.</p>
+ **Change**, fix or implement something.<p>Tests: Make sure to always run `nosetests` (in the projects `src/` directory) before commiting. We also use the [black codeformatter][code-black] (`pip install black`) - run `black .`</p>
+ Submit a **pull request**.<p>They'll likely be *merged* and you'll definitely get some *feedback*.</p>

### Other ways to help

You can also [contact Finn][contact] or [sponsor this project :heart:][sponsor]!

<a id="license"></a>
## License

[MIT License. Copyright 2020 Finn M Glas.][MIT]

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
  [shield-star]: https://img.shields.io/github/stars/finnmglas/LedgerMan?label=Star&style=social

  [shield-fork]: https://img.shields.io/github/forks/finnmglas/LedgerMan?label=Fork&style=social

<!-- Python Package -->
  [pypi]: https://pypi.org/project/ledgerman/
  [pypi-version-badge]: https://img.shields.io/pypi/v/ledgerman?color=000

  [pepy tech]: https://pepy.tech/project/ledgerman
  [pepi-downloads-badge]: https://img.shields.io/badge/dynamic/json?style=flat&color=000&maxAge=10800&label=downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Fledgerman

  [code-black]: https://github.com/psf/black
  [code-black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg

<!-- Legal -->
  [MIT]: https://choosealicense.com/licenses/mit/
