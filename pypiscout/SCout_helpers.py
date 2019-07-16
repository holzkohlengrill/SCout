"""
SCout | Special Character Out

Copyright 2017-2019, Marcel Schmalzl (MSc)
This code is licensed under a MIT license
You should have received a copy of the MIT licence along with this program.
If not see:
* https://github.com/holzkohlengrill/SCout/blob/master/LICENSE
* https://opensource.org/licenses/MIT
"""

import sys


class Singleton(type):
    """
    Singleton metaclass
    """
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        # FIXME: It would be prettier if we can change the settings via `sc(<params>)`
        #       the following code would allow this however we would get a change to default values for a call like `sc().header("test")`
        #       `chgSettings()` would then do the same like the current implementation of `Logger.__call__(self, invVerbosity: int = 0, actionWarning=None, actionError=None)`
        # else:
        #     cls.__instances[cls].chgSettings(*args, **kwargs)
        return cls.__instances[cls]


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


class Colours:
    """
    Colour definitions
    """
    WHITE = '\033[37m'          # Indeed very light grey
    LIGHT_CYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'        # Yellow
    WWARNING = '\033[33m'       # Dark Grey
    ERROR = '\033[91m'          # Light red
    HEADER = '\033[1m'          # Bold white
    UNDERLINE = '\033[4m'

    NO_COLOUR = '\033[0m'


def _checkNconvertStr(texts):
    """
    Checks whether input is a string or if it can be casted into one
    :param texts: A string or a type which can be converted into one
    :return: Text as a string if successful otherwise nothing (exception)
    """
    concatTextLst = []
    for text in texts:
        # Test texts elements
        tempText = str(text)
        if type(tempText) is not str:
            raise TypeError("Input type must be a string or convertible into a string")
        concatTextLst.append(str(text))

    return " ".join(concatTextLst)      # Preserve whitespaces when using multiple text elements
