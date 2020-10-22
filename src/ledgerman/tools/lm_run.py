#! /usr/bin/python3

import argparse, sys, re

try:
    import readline
except:
    pass  # readline not available


class PyMoney:
    """
    'ledgerman run' / 'pymoney' is a commandline tool, that extends pythons syntax
    to simplify financial calculations using the LedgerMan Python module.
    """

    class regex:
        """
        Some common regular expressions from the PyMoney syntax.
        """

        white = "[ \t]+"
        num = "([-+]?[0-9]*\.?[0-9]+)"
        currency = "([A-Z]+)"
        money = num + white + currency

    @staticmethod
    def error(e):
        PyMoney.parser.error(e)

    @staticmethod
    def generateParser():
        """
        Generate the ArgumentParser for 'pymoney'.
        """
        PyMoney.parser = argparse.ArgumentParser(
            prog="ledgerman run",
            description="Execute PyMoney-syntax-extended python code.",
            epilog="More details at https://github.com/finnmglas/LedgerMan#tools-pymoney-syntax",
        )
        PyMoney.parser.add_argument(
            "script", nargs="?", default=None, help="A PyMoney script to execute."
        )

        return PyMoney.parser

    @staticmethod
    def main(args=None):
        """
        The main program of 'pymoney'.
        """
        if args == None:  # parse args using own parser
            PyMoney.generateParser()
            args = PyMoney.parser.parse_args(sys.argv[1:])

        # main
        if args.script == None:
            PyMoney.runShell()
            return

        try:
            f = open(args.script)
        except FileNotFoundError:
            print("File not found.")
            exit()

        code = f.read()
        f.close()
        PyMoney.execute(code)

    # PyMoney functions

    @staticmethod
    def runShell():
        """
        Run a PyMoney shell loop.
        """
        PyMoney.execute("from ledgerman import *")

        shouldRun = True
        print(
            "Welcome to the PyMoney Shell by @finnmglas\n"
            + "Details at https://github.com/finnmglas/ledgerman"
        )
        while shouldRun:
            try:
                cmd = input(">>> ")
                if cmd == "":
                    continue
                out = PyMoney.evaluate(cmd)
                if type(out) != type(None):
                    print(out)
            except KeyboardInterrupt:
                print("\nKeyboardInterrupt")
            except EOFError:
                print("\nExiting...")
                shouldRun = False
            except Exception as e:
                print(e)

    @staticmethod
    def evaluate(code):
        """
        Evaluate code with PyMoney syntax (shell).
        """
        return eval(PyMoney.convert(code), globals())

    @staticmethod
    def execute(code):
        """
        Execute code with PyMoney syntax.
        """
        return exec(PyMoney.convert(code), globals())

    @staticmethod
    def convert(code):
        """
        Convert PyMoney syntax to regular executable python.
        """
        # implement Conversion syntax `EUR => 1.17 USD`
        code = re.sub(
            PyMoney.regex.currency
            + PyMoney.regex.white
            + "=>"
            + PyMoney.regex.white
            + PyMoney.regex.money,
            r'Money.addExchangeRate("\1", "\3", \2)',
            code,
        )
        # implement Money syntax `X.X EUR`
        code = re.sub(PyMoney.regex.money, r'Money(\1, "\2")', code)

        return code


if __name__ == "__main__":
    PyMoney.main()
