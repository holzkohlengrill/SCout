# Special Character Out class
# Author: Marcel Schmalzl (MSc)


# TODO: use coloured output; yellow/orange for warnings, red for errors

class SCout:
    """
    Special Character Out (formatted)
    """
    @staticmethod
    def _checkNconvertStr(texts):
        """
        checks whether input is a string or if it can be casted into one
        :param texts: a string or a type which can be converted into one
        :return: text as a string if successful otherwise nothing (exception)
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
        prints a info message (usable like normal print)
        :param text: see doc of `_checkNconvertStr`
        :return: formatted text to standard output
        """
        print('(info) : '.rjust(12), SCout._checkNconvertStr(text))

    @staticmethod
    def warning(*text):
        """
        prints a warning message (usable like normal print)
        :param text: see doc of `_checkNconvertStr`
        :return: formatted text to standard output
        """
        print('(warning) : '.rjust(12), SCout._checkNconvertStr(text))

    @staticmethod
    def error(*text):
        """
        prints an error message (usable like normal print)
        :param text: see doc of `_checkNconvertStr`
        :return: formatted text to standard output
        """
        print('(error) : '.rjust(12), SCout._checkNconvertStr(text))
