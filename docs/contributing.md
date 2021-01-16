# Contributing

If you can't help with the development (you're busy, whatever...), make sure to ***star this repository***, as that helps other developers find LedgerMan:

[![][shield-star]][star]

You can also join our [discord]!

<a id="contributing-code"></a>
## Contributing Code

If you want to contribute code, make sure you keep the class structure the same. Generally:

```python
# --- STATIC VARIABLES --- #
# --- STATIC METHODS --- #
# --- DATA MODEL METHODS --- #
# --- CLASS SPECIFIC METHODS --- #
# --- DATA MODEL OPERATIONS --- #
```

+ **Fork** this repository:
<br><p style="margin-left:30px;">[![][shield-fork]][fork]</p>
+ **Set up** the environment:<p>Run `pip install -e .` in LedgerMan's `src/` for a development installation.</p>
+ **Change**, fix or implement something.<p>Tests: Make sure to always run `nosetests` (in the projects `src/` directory) before commiting. We also use the [black codeformatter][code-black] (`pip install black`) - run `black .`</p>
+ Submit a **pull request**.<p>They'll likely be *merged* and you'll definitely get some *feedback*.</p>

## Other ways to help

You can also [contact Finn][contact] or [sponsor this project ❤️][sponsor]!

<a id="license"></a>
# License

[MIT License. Copyright 2020 Finn M Glas.][MIT]

  [contact]: https://contact.finnmglas.com
  [sponsor]: https://sponsor.finnmglas.com
  [discord]: https://discord.com/invite/BsZXaur
  [joingh]: https://github.com/join
  [newissue]: https://github.com/glastrading/ledgerman/issues/new/choose
  [fork]: https://github.com/glastrading/ledgerman/fork
  [star]: https://github.com/glastrading/ledgerman/stargazers
  [shield-star]: https://img.shields.io/github/stars/finnmglas/LedgerMan?label=Star&style=social
  [shield-fork]: https://img.shields.io/github/forks/finnmglas/LedgerMan?label=Fork&style=social
  [code-black]: https://github.com/psf/black
  [MIT]: https://choosealicense.com/licenses/mit/
