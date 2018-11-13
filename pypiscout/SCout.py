#####################################
# SCout | Special Character Out
# Author: Marcel Schmalzl (MSc)
#####################################

_VERSION_MAJOR = "1"
_VERSION_MINOR = "8"
VERSION = ".".join([_VERSION_MAJOR, _VERSION_MINOR])

# MIT License
# Copyright (c) 2016-2018 Marcel Schmalzl

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys

"""
Special Character Out (formatted)
"""


def _canUseColour():
    """
    Checks if coloured text output is supported
    :return: True if colours are supported, otherwise False
    """
    supportedPlatforms = ["linux", "cygwin", "darwin"]
    platformSupported = False

    for platform in supportedPlatforms:
        if sys.platform.startswith(platform):
            platformSupported = True
            break

    isTty = hasattr(sys.stdout, 'isatty') and not sys.stdout.isatty()
    if platformSupported or isTty:
        return True
    else:
        return False


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
        neededLength = len(text) + 8                          # Two spaces + 3 x 2 slashes
        return symbol * neededLength

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

        return " ".join([symbol * 3, text, symbol * 3])       # 3 synbols + text + 3 symbols separated by spaces

    @staticmethod
    def gen(text, symbol="/"):
        """
        Generate a header
        :param text: Text
        :param symbol: Symbol (default: "/")
        :return: Header as string
        """
        return Header._genTopBottom(text, symbol) + "\n" + Header._genMiddle(text, symbol) + "\n" + Header._genTopBottom(text, symbol) + "\n"


class Colours:
    """
    Colour definitions
    """
    WHITE = '\033[37m'          # Indeed very light grey
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'        # Yellow
    ERROR = '\033[91m'          # Light red
    HEADER = '\033[1m'          # Bold white
    UNDERLINE = '\033[4m'


def _checkNconvertStr(texts):
    """
    Checks whether input is a string or if it can be casted into one
    :param texts: A string or a type which can be converted into one
    :return: Text as a string if successful otherwise nothing (exception)
    """
    concatText = str()
    concatTextLst = []
    for text in texts:
        # Test texts elements
        tempText = str(text)
        if type(tempText) is not str:
            raise TypeError("Input type must be a string or convertible into a string")
        concatTextLst.append(str(text))

    return " ".join(concatTextLst)      # Preserve whitespaces when using multiple text elements


def info(*text, disableColour = False):
    """
    Prints a info message (usable like normal print)
    :param text: See doc of `_checkNconvertStr`
    :return: nothing
    """
    stdColour = ""
    if _canUseColour() and not disableColour:
        stdColour = Colours.WHITE
    textOut = " ".join(['(info) : '.rjust(12), _checkNconvertStr(text) + stdColour])
    print(textOut)
    return textOut


def warning(*text, disableColour = False):
    """
    Prints a warning message (usable like normal print)
    :param text: See doc of `_checkNconvertStr`
    :return: nothing
    """
    colour = ""
    stdColour = ""
    if _canUseColour() and not disableColour:
        colour = Colours.WARNING
        stdColour = Colours.WHITE
    textOut = " ".join([colour + '(warning) : '.rjust(12), _checkNconvertStr(text) + stdColour])
    print(textOut)
    return textOut


def error(*text, disableColour = False):
    """
    Prints an error message (usable like normal print)
    :param text: See doc of `_checkNconvertStr`
    :return: nothing
    """
    colour = ""
    stdColour = ""
    if _canUseColour() and not disableColour:
        colour = Colours.ERROR
        stdColour = Colours.WHITE
    textOut = " ".join([colour + '(error) : '.rjust(12), _checkNconvertStr(text) + stdColour])
    print(textOut)
    return textOut


def header(*text, symbol="/", disableColour = False):
    """
    Prints a header in the following style

    :param text: Header text
    :param symbol: Symbol used for header (default: "/")
    :return: nothing
    """
    colour = ""
    stdColour = ""
    if _canUseColour() and not disableColour:
        colour = Colours.BLUE
        stdColour = Colours.WHITE
    textOut = " ".join([colour + Header.gen(_checkNconvertStr(text), symbol=symbol) + stdColour])
    print(textOut)
    return textOut
