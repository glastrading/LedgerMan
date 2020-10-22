#! /usr/bin/python3

import argparse, sys


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

        print(args.rates)


if __name__ == "__main__":
    LedgerMan.main()
