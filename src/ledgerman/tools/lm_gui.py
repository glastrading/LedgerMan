#! /usr/bin/python3

import argparse, sys, wx

from ledgerman import *


class LedgerManGui:

    """
    The LedgerMan gui.
    """

    @staticmethod
    def error(e):
        LedgerManGui.parser.error(e)

    @staticmethod
    def generateParser():

        """
        Generate the ArgumentParser for 'ledgerman gui'.
        """

        LedgerManGui.parser = argparse.ArgumentParser(
            prog="ledgerman gui",
            description="The 'ledgerman-convert' tool coverts and adds currencies.",
            epilog="More details at https://github.com/finnmglas/LedgerMan#tools-convert.",
        )

        return LedgerManGui.parser

    @staticmethod
    def main(args=None):

        """
        The main program of 'ledgerman gui'.
        """

        if args == None:  # parse args using own parser
            LedgerManGui.generateParser()
            args = LedgerManGui.parser.parse_args(sys.argv[1:])

        app = wx.App()
        window = wx.Frame(None, title="wxPython Frame", size=(300, 200))
        panel = wx.Panel(window)
        label = wx.StaticText(panel, label="Hello World", pos=(100, 50))
        window.Show(True)
        app.MainLoop()


if __name__ == "__main__":
    LedgerMan.main()
