
class color:

    """
    An enumeration of common colors.
    """

    class foreground:

        """
        Foreground color codes.
        """

        RED = red = "\033[31m"
        GREEN = green = "\033[32m"
        YELLOW = yellow = "\033[33m"
        BLUE = blue = "\033[34m"
        WHITE = white = "\033[37m"

        BOLD = bold = "\033[1m"
        UNDERLINE = underline = "\033[4m"

    class background:

        """
        Background color codes.
        """

        RED = red = "\033[41m"
        GREEN = green = "\033[42m"
        YELLOW = yellow = "\033[43m"
        BLUE = blue = "\033[44m"
        WHITE = white = "\033[47m"

    END = "\033[0m"
