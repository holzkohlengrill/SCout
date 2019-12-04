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
_VERSION_PATCH = "1"
VERSION = ".".join([_VERSION_MAJOR, _VERSION_MINOR, _VERSION_PATCH])


class Logger(metaclass=Singleton):
    """
    SCout logging class
    """
    @staticmethod
    def _checkVerbosity(invVerbosity):
        """
        Check for valid values of invVerbosity (if invalid an exception is thrown)
        :param invVerbosity: [int or str]
        :return: None
        """
        # Verbosity sanity checks
        if type(invVerbosity) is str:
            if invVerbosity == "":                              # Must be the first str check
                raise ValueError("Passed empty string!")
            if invVerbosity.isdigit():
                # Everything O.K.
                pass
            else:
                # If negative number
                if invVerbosity[0] == "-":
                    # If rest is a number
                    if invVerbosity[1:].isdigit():
                        # Everything O.K.
                        pass
                    else:
                        raise ValueError("Passed str could not be converted to int!")
                # First character is illegal
                else:
                    raise ValueError("Passed invalid str!")
        elif type(invVerbosity) is int:
            pass
        else:
            raise TypeError("Type must be either str or int!")

    class Settings:
        """
        Initialises generic settings:
         * invVerbosity level
         * actions if an error or warning occurred (provide a function to set behaviour)
        """
        def __init__(self, invVerbosity, actionWarning, actionError):
            """
            Initialise settings
            Arguments: see Logger.__init__ docstring
            """
            self.invVerbosity = invVerbosity
            self.actionWarning = actionWarning
            self.actionError = actionError

    def __init__(self, invVerbosity = 0, actionWarning=None, actionError=None):
        """
        Set settings - only called once (later it is __call__)
        :param invVerbosity: [int or str] Inverse invVerbosity levels: (default: 0)
                        -1  : Print all (debug, info, weak warnings, warning & error)
                        0   : Print info, weak warnings, warning & error
                        1   : Print weak warnings, warning & error
                        2   : Print warning & error
                        3   : Print error
                        4   : Do NOT print anything
        :param actionWarning: Provide a function which is executed in case of a warning (default: None)
        :param actionError: Provide a function which is executed in case of an error (default: None)
        """
        Logger._checkVerbosity(invVerbosity)
        # If every check went fine do conversion to int
        invVerbosity = int(invVerbosity)                                                        # Convert to int since it might come as string through argument parsing
        self.__settings = Logger.Settings(invVerbosity, actionWarning, actionError)

    def __call__(self, invVerbosity: int = 0, actionWarning=None, actionError=None):
        """
        Exactly like init
        This callable let the user change the settings later on
        """
        Logger._checkVerbosity(invVerbosity)
        # If every check went fine do conversion to int
        invVerbosity = int(invVerbosity)                                                        # Convert to int since it might come as string through argument parsing
        self.__settings = Logger.Settings(invVerbosity, actionWarning, actionError)


    def debug(self, *text, disableColour=False):
        """
        Debug (print defug information)
        :param text: See doc of `_checkNconvertStr`
        :param disableColour: disable coloured output (default: False)
        :return: The text printed
        """
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
