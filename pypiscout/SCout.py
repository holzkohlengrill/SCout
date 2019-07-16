"""
SCout | Special Character Out

Copyright 2017-2019, Marcel Schmalzl (MSc)
This code is licensed under a MIT license
You should have received a copy of the MIT licence along with this program.
If not see:
* https://github.com/holzkohlengrill/SCout/blob/master/LICENSE
* https://opensource.org/licenses/MIT
"""

from pypiscout.SCout_helpers import _canUseColour, _checkNconvertStr, Colours

__ALIGNMENT = 16


class Header:
    """
    Generate header
    """
    @staticmethod
    def _genTopBottom(text, symbol):
        """
        Generate the top or bottom of the header
        :param text: Text
        :param symbol: Symbol
        :return: String for top + bottom header
        """
        neededLength = len(text) + 8  # Two spaces + 3 x 2 slashes
        return str(symbol * neededLength)

    @staticmethod
    def _genMiddle(text, symbol):
        """
        Generate the middle of the header
        :param text: Text
        :param symbol: Symbol
        :return: String for middle header
        """
        # TODO: Add multi-line support (MSc)
        # Workaround:
        if "\n" in "".join(text):
            for txt in text:
                txt.replace("\n", "; ")
            print(text)

        return " ".join([symbol * 3, text, symbol * 3])  # 3 synbols + text + 3 symbols separated by spaces

    @staticmethod
    def gen(text, symbol="/"):
        """
        Generate a header
        :param text: Text
        :param symbol: Symbol (default: "/")
        :return: Header as string
        """
        return Header._genTopBottom(text, symbol) + "\n" + Header._genMiddle(text, symbol) + "\n" + Header._genTopBottom(text, symbol) + "\n"


def debug(*text, disableColour=False):
    """
    Prints a debug message (usable like normal print)
    :param disableColour: disable coloured output (default: False)
    :param text: See doc of `_checkNconvertStr`
    :return: The text printed
    """
    colour = ""
    stdColour = ""
    if _canUseColour() and not disableColour:
        colour = Colours.LIGHT_CYAN
        stdColour = Colours.NO_COLOUR
    textOut = " ".join([colour + '(debug) :'.rjust(__ALIGNMENT), _checkNconvertStr(text) + stdColour])
    print(textOut)
    return textOut


def info(*text, disableColour=False):
    """
    Prints a info message (usable like normal print)
    :param disableColour: disable coloured output (default: False)
    :param text: See doc of `_checkNconvertStr`
    :return: The text printed
    """
    colour = ""
    stdColour = ""
    if _canUseColour() and not disableColour:
        colour = Colours.WHITE
        stdColour = Colours.NO_COLOUR
    textOut = " ".join([colour + ' (info) :'.rjust(__ALIGNMENT), _checkNconvertStr(text) + stdColour])
    print(textOut)
    return textOut


def wwarning(*text, disableColour=False):
    """
    Prints a weak warning message (usable like normal print)
    :param disableColour: disable coloured output (default: False)
    :param text: See doc of `_checkNconvertStr`
    :return: The text printed
    """
    colour = ""
    stdColour = ""
    if _canUseColour() and not disableColour:
        colour = Colours.WWARNING
        stdColour = Colours.NO_COLOUR
    textOut = " ".join([colour + '(weak warning) :'.rjust(__ALIGNMENT), _checkNconvertStr(text) + stdColour])
    print(textOut)
    return textOut


def warning(*text, disableColour=False):
    """
    Prints a warning message (usable like normal print)
    :param disableColour: disable coloured output (default: False)
    :param text: See doc of `_checkNconvertStr`
    :return: The text printed
    """
    colour = ""
    stdColour = ""
    if _canUseColour() and not disableColour:
        colour = Colours.WARNING
        stdColour = Colours.NO_COLOUR
    textOut = " ".join([colour + '(warning) :'.rjust(__ALIGNMENT), _checkNconvertStr(text) + stdColour])
    print(textOut)
    return textOut


def error(*text, disableColour=False):
    """
    Prints an error message (usable like normal print)
    :param disableColour: disable coloured output (default: False)
    :param text: See doc of `_checkNconvertStr`
    :return: The text printed
    """
    colour = ""
    stdColour = ""
    if _canUseColour() and not disableColour:
        colour = Colours.ERROR
        stdColour = Colours.NO_COLOUR
    textOut = " ".join([colour + '(error) :'.rjust(__ALIGNMENT), _checkNconvertStr(text) + stdColour])
    print(textOut)
    return textOut


def custom(*text, disableColour=False, colourCode=Colours.WHITE, prefix='info', alignment=__ALIGNMENT):
    """
    Prints a customised message (usable like normal print)
    :param text:  See doc of `_checkNconvertStr`
    :param disableColour: disable coloured output (default: False)
    :param colourCode: custom colour (int of foreground colour ANSI/VT100 Control sequence) (default: white)
    :param prefix: Text to display like `warning`, `error`, `info`, ... (default: info)
    :param alignment: Padding of text vs. prefix
    :return: The text printed
    """
    colour = ""
    stdColour = ""
    if _canUseColour() and not disableColour:
        colour = '\033[' + colourCode + 'm'
        stdColour = Colours.NO_COLOUR
    textOut = " ".join([colour + '(' + str(prefix) + ') :'.rjust(alignment), _checkNconvertStr(text) + stdColour])
    print(textOut)
    return textOut


def header(*text, symbol="/", disableColour=False):
    """
    Prints a header in the following style
    :param disableColour: disable coloured output (default: False)
    :param text: Header text
    :param symbol: Symbol used for header (default: "/")
    :return: The text printed
    """
    colour = ""
    stdColour = ""
    if _canUseColour() and not disableColour:
        colour = Colours.BLUE
        stdColour = Colours.NO_COLOUR
    textOut = " ".join([colour + Header.gen(_checkNconvertStr(text), symbol=symbol) + stdColour])
    print(textOut)
    return textOut
