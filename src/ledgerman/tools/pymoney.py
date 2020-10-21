#! /usr/bin/python3

import argparse, sys, re

try:
    import readline
except:
    pass  # readline not available


class PyMoney:
    """
    PyMoney is a Python syntax extender and commandline tool.
    It is used to simplify financial calculus using the ledgerman module.
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
    def parse_args(argv):
        """
        Parse the commandline arguments for the PyMoney tool.
        """
        parser = argparse.ArgumentParser(
            description="Execute PyMoney-extended python code."
        )
        parser.add_argument(
            "file", nargs="?", default=None, help="A pymoney file to execute."
        )

        return parser.parse_args(argv)

    @staticmethod
    def main():
        args = PyMoney.parse_args(sys.argv[1:])

        if args.file == None:
            PyMoney.runShell()
        else:
            try:
                f = open(args.file)
            except FileNotFoundError:
                print("File not found.")
                exit()
            code = f.read()
            f.close()
            PyMoney.execute(code)

    def runShell():
        PyMoney.execute("from ledgerman import *")

        shouldRun = True
        print(
            "Welcome to the PyMoney Shell by @finnmglas\nDetails at https://github.com/finnmglas/ledgerman"
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