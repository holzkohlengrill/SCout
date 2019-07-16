"""
SCout | Special Character Out

Copyright 2017-2019, Marcel Schmalzl (MSc)
This code is licensed under a MIT license
You should have received a copy of the MIT licence along with this program.
If not see:
* https://github.com/holzkohlengrill/SCout/blob/master/LICENSE
* https://opensource.org/licenses/MIT
"""

from pypiscout.SCout import header, debug, info, wwarning, warning, error
from pypiscout.SCout_helpers import Singleton

_VERSION_MAJOR = "2"
_VERSION_MINOR = "0"
VERSION = ".".join([_VERSION_MAJOR, _VERSION_MINOR])


class Logger(metaclass=Singleton):
    """
    SCout logging class
    """
    class Settings:
        """
        Initialises generic settings:
         * invVerbosity level
         * actions if an error or warning occurred (provide a function to set behaviour)
        """
        def __init__(self, invVerbosity: int, actionWarning, actionError):
            """
            Initialise settings
            Arguments: see Logger.__init__ docstring
            """
            self.invVerbosity = invVerbosity
            self.actionWarning = actionWarning
            self.actionError = actionError

    def __init__(self, invVerbosity: int = 0, actionWarning=None, actionError=None):
        """
        Set settings
        :param invVerbosity: Inverse invVerbosity levels: (default: 0)
                        -1  : Print all (debug, info, weak warnings, warning & error)
                        0   : Print info, weak warnings, warning & error
                        1   : Print weak warnings, warning & error
                        2   : Print warning & error
                        3   : Print error
                        4   : Do NOT print anything
        :param actionWarning: Provide a function which is executed in case of a warning (default: None)
        :param actionError: Provide a function which is executed in case of an error (default: None)
        """
        self.__settings = Logger.Settings(invVerbosity, actionWarning, actionError)

    def __call__(self, invVerbosity: int = 0, actionWarning=None, actionError=None):
        """
        Exactly like init
        This callable let the user change the settings later on
        """
        self.__settings = Logger.Settings(invVerbosity, actionWarning, actionError)

    def debug(self, *text, disableColour=False):
        if 1 > self.__settings.invVerbosity:
            return debug(*text, disableColour=disableColour)

    def info(self, *text, disableColour=False):
        """
        Info (general information to be printed)
        :param disableColour: disable coloured output (default: False)
        :param text: See doc of `_checkNconvertStr`
        :return: The text printed
        """
        if 2 > self.__settings.invVerbosity:
            return info(*text, disableColour=disableColour)

    def warning(self, *text, disableColour=False):
        """
        Warning
        :param disableColour: disable coloured output (default: False)
        :param text: See doc of `_checkNconvertStr`
        :return: The text printed
        """
        if 3 > self.__settings.invVerbosity:
            return warning(*text, disableColour=disableColour)
        if self.__settings.actionWarning:
            self.__settings.actionWarning()

    def wwarning(self, *text, disableColour=False):
        """
        Weak warning (like warning but less prominent)
        Does not have an associated warning action
        :param disableColour: disable coloured output (default: False)
        :param text: See doc of `_checkNconvertStr`
        :return: The text printed
        """
        if 3 > self.__settings.invVerbosity:
            return wwarning(*text, disableColour=disableColour)

    def error(self, *text, disableColour=False):
        """
        Error message (something prevents the application from continuing)
        :param disableColour: disable coloured output (default: False)
        :param text: See doc of `_checkNconvertStr`
        :return: The text printed
        """
        if 4 > self.__settings.invVerbosity:
            error(*text, disableColour=disableColour)
        if self.__settings.actionError:
            self.__settings.actionError()

    def header(self, *text, symbol="/", disableColour=False):
        """
        Header (title alike)
        :return: The text printed
        :param text: See doc of `_checkNconvertStr`
        :param symbol: Character decorating the header (default: "/")
        :param disableColour: disable coloured output (default: False)
        :return: The text printed
        """
        if 5 > self.__settings.invVerbosity:
            return header(*text, symbol=symbol, disableColour=disableColour)
