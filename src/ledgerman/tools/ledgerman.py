#! /usr/bin/python3

import argparse, sys

from .lm_convert import LedgerManConvert


class LedgerMan:
    """
    The 'ledgerman' commandline tool based on the LedgerMan python module.
    It parses input and chooses which LedgerMan tool to execute.
    """

    tools = {"convert": LedgerManConvert}

    @staticmethod
    def error(e):
        LedgerMan.parser.error(e)

    @staticmethod
    def generateParser():
        """
        Generate the ArgumentParser for 'ledgerman'.
        """
        LedgerMan.parser = argparse.ArgumentParser(
            description="LedgerMan calculates and manages finances.",
            epilog="More details at https://github.com/finnmglas/LedgerMan.",
        )

        subparsers = LedgerMan.parser.add_subparsers(
            dest="tool", help="LedgerMan tools"
        )
        subparsers.required = True

        for name in LedgerMan.tools:
            tool = LedgerMan.tools[name]
            # Import Parser --- ledgerman [name]
            toolParser = subparsers.add_parser(name)
            toolParser.__dict__ = tool.generateParser().__dict__

        return LedgerMan.parser

    @staticmethod
    def main():
        # generate parser
        LedgerMan.generateParser()
        # parse args
        args = LedgerMan.parser.parse_args(sys.argv[1:])
        # forward args to a tool
        LedgerMan.tools[args.tool].main(args)


if __name__ == "__main__":
    LedgerMan.main()
