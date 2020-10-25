from setuptools import setup

long_description = """
|PyPI - Version| |Downloads| |Discord| |Code style: black|

LedgerMan
=========

   Yet another python library for finance. **Why?**

-  LedgerMan is **comprehensive**. Check out `its usage`_!
-  LedgerMan is **open, welcoming and transparent**: `join us on
   discord`_!
-  LedgerMan provides **powerful** financial tools and models.

=====

`View on GitHub`_, `contact Finn`_ or `sponsor this project ❤️`_!

.. _its usage: https://github.com/finnmglas/ledgerman#usage
.. _join us on discord: https://discord.com/invite/BsZXaur
.. _View on GitHub: https://github.com/finnmglas/ledgerman
.. _contact Finn: https://contact.finnmglas.com
.. _sponsor this project ❤️: https://sponsor.finnmglas.com

.. |PyPI - Version| image:: https://img.shields.io/pypi/v/ledgerman?color=000
   :target: https://pypi.org/project/ledgerman/
.. |Downloads| image:: https://img.shields.io/badge/dynamic/json?style=flat&color=000&maxAge=10800&label=downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Fledgerman
   :target: https://pepy.tech/project/ledgerman
.. |Discord| image:: https://img.shields.io/badge/discord-join%20chat-000
   :target: https://discord.com/invite/BsZXaur
.. |Code style: black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
"""

setup(
    name="ledgerman",
    version="0.6.0",
    description="The python library for accounting and finance.",
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial :: Accounting",
    ],
    keywords="accounting finance manager money library ledger ledgerman crypto",
    url="http://github.com/finnmglas/LedgerMan",
    author="Finn M Glas",
    author_email="finn@finnmglas.com",
    license="MIT",
    packages=["ledgerman"],
    entry_points={
        "console_scripts": [
            "ledgerman=ledgerman.tools:LedgerMan.main",
        ],
    },
    install_requires=["requests", "argparse"],
    test_suite="nose.collector",
    tests_require=["nose"],
    include_package_data=True,
    zip_safe=False,
)
