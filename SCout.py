# Special Character Out class v0.3
# Author: Marcel Schmalzl (MSc)

# MIT License
# Copyright (c) 2016 Marcel Schmalzl

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


# TODO: use coloured output; yellow/orange for warnings, red for errors

class SCout:
    """
    Special Character Out (formatted)
    """
    @staticmethod
    def _checkNconvertStr(texts):
        """
        Checks whether input is a string or if it can be casted into one
        :param texts: A string or a type which can be converted into one
        :return: Text as a string if successful otherwise nothing (exception)
        """
        concatText = str()
        for text in texts:
            tempText = str(text)
            if type(tempText) is not str:
                raise TypeError("Input type must be a string or convertible into a string")
            concatText += tempText
            concatText += " "       # add space at the end
        return concatText

    @staticmethod
    def info(*text):
        """
        Prints a info message (usable like normal print)
        :param text: See doc of `_checkNconvertStr`
        :return: Formatted text to standard output
        """
        print('(info) : '.rjust(12), SCout._checkNconvertStr(text))

    @staticmethod
    def warning(*text):
        """
        Prints a warning message (usable like normal print)
        :param text: See doc of `_checkNconvertStr`
        :return: Formatted text to standard output
        """
        print('(warning) : '.rjust(12), SCout._checkNconvertStr(text))

    @staticmethod
    def error(*text):
        """
        Prints an error message (usable like normal print)
        :param text: See doc of `_checkNconvertStr`
        :return: Formatted text to standard output
        """
        print('(error) : '.rjust(12), SCout._checkNconvertStr(text))
