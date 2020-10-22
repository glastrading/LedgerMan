#! /usr/bin/python3

import argparse, sys

from ledgerman import *
from .lm_run import PyMoney


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
            "expression", nargs="?", help="An expression to be converted."
        )
        LedgerManConvert.parser.add_argument(
            "currency", nargs="?", help="The currency to convert to."
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

        if args.expression:
            if (
                len(args.expression.split(" ")) == 1
                and args.expression.upper() == args.expression
            ):
                args.expression = "1 " + args.expression

            try:
                expression = PyMoney.evaluate(args.expression, globals())
            except SyntaxError:
                LedgerManConvert.error(
                    "SyntaxError in expression '" + args.expression + "'."
                )
            except:
                LedgerManConvert.error(
                    "Unexpected expression '" + args.expression + "'."
                )

        if args.currency:
            if len(args.currency.split(" ")) == 1:
                currency = args.currency
            else:
                LedgerManConvert.error(
                    "Unrecognized destination currency: '" + args.currency + "'."
                )

            try:
                print(
                    args.expression, "=", Money.exchange.convert(expression, currency)
                )
            except ValueError:
                LedgerManConvert.error(
                    "Can't convert '"
                    + args.expression
                    + "' to '"
                    + args.currency
                    + "'."
                )
        else:
            print(expression)


if __name__ == "__main__":
    LedgerMan.main()
