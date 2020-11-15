#! /usr/bin/python3

import argparse, sys, wx

from ledgerman import *


class LedgerManGUI:

    """
    The LedgerMan gui.
    """

    @staticmethod
    def error(e):
        LedgerManGUI.parser.error(e)

    @staticmethod
    def generateParser():

        """
        Generate the ArgumentParser for 'ledgerman gui'.
        """

        LedgerManGUI.parser = argparse.ArgumentParser(
            prog="ledgerman gui",
            description="LedgerMan's graphical user interface.",
            epilog="More details at https://github.com/finnmglas/LedgerMan",
        )

        return LedgerManGUI.parser

    @staticmethod
    def main(args=None):

        """
        The main program of 'ledgerman gui'.
        """

        if args == None:  # parse args using own parser
            LedgerManGUI.generateParser()
            args = LedgerManGUI.parser.parse_args(sys.argv[1:])

        from .main import main

        main()


if __name__ == "__main__":
    LedgerMan.main()
