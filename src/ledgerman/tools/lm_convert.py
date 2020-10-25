#! /usr/bin/python3

import argparse, sys

from ledgerman import *


class LedgerManConvert:

    """
    'ledgerman convert' is a commandline tool, that converts currencies.
    """

    @staticmethod
    def error(e):
        LedgerManConvert.parser.error(e)

    @staticmethod
    def generateParser():

        """
        Generate the ArgumentParser for 'ledgerman convert'.
        """

        LedgerManConvert.parser = argparse.ArgumentParser(
            prog="ledgerman convert",
            description="The 'ledgerman-convert' tool coverts and adds currencies.",
            epilog="More details at https://github.com/finnmglas/LedgerMan#tools-convert.",
        )
        LedgerManConvert.parser.add_argument(
            "--rates",
            help="Fetch and print all exchange rates.",
            action="store_true",
            default=False,
        )
        LedgerManConvert.parser.add_argument(
            "source", nargs="?", help="The currency to convert from."
        )
        LedgerManConvert.parser.add_argument(
            "dest", nargs="?", help="The currency to convert to."
        )

        return LedgerManConvert.parser

    @staticmethod
    def main(args=None):

        """
        The main program of 'ledgerman convert'.
        """

        if args == None:  # parse args using own parser
            LedgerManConvert.generateParser()
            args = LedgerManConvert.parser.parse_args(sys.argv[1:])

        # fetch
        Money.fetchRates("ecb")  # European Central Bank
        Money.fetchRates("coingecko")  # Crypto

        # interpret
        if args.rates:  # ledgerman convert --rates
            for rate in Money.exchange.exchangeRates:
                print(rate)
            exit()

        if args.source and args.dest:
            print(Money("1 " + args.source, roundTo="0.000001").to(args.dest))


if __name__ == "__main__":
    LedgerMan.main()
