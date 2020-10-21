from setuptools import setup

long_description = """

Ledgerman
=========

|PyPI - Version| |Downloads| |Discord| |Code style: black|

(𝙣𝙚𝙬) Financial calculations, models and tools in a comprehensive and feature-packed python library!

`Learn using the library on GitHub <https://github.com/finnmglas/ledgerman>`__ or
`Contact Finn <https://www.finnmglas.com/contact>`__

.. |PyPI - Version| image:: https://img.shields.io/pypi/v/ledgerman?color=000
   :target: https://pypi.org/project/ledgerman/
.. |Downloads| image:: https://img.shields.io/badge/dynamic/json?style=flat&color=000&maxAge=10800&label=downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2fledgerman
   :target: https://pepy.tech/project/ledgerman
.. |Discord| image:: https://img.shields.io/badge/discord-join%20chat-000000.svg
   :target: https://discord.com/invite/BsZXaur
.. |Code style: black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
"""

setup(
    name="ledgerman",
    version="0.4.0",
    description="Yet another python library for finance.",
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
        "console_scripts": ["pymoney=ledgerman.tools:PyMoney.main"],
    },
    install_requires=["requests"],
    test_suite="nose.collector",
    tests_require=["nose"],
    include_package_data=True,
    zip_safe=False,
)
