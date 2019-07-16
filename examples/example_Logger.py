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

from pypiscout.SCout_Logger import Logger as sc

"""
No specific settings:
* invVerbosity=0,
* actionWarning=None,
* actionError=None
"""

print("\n")

# Implicit construction with default settings during first call; to make it more readable call `sc()` upfront or use simple SCout
sc().header("Simple SCout")
sc().debug("Some debug message:", "0xDEADBEEF")
sc().info("An info message")
sc().wwarning("Weak warnings are supported")
sc().warning("This is a warning")
sc().error("An error occurred")

print("\n----\n")

# Edit current settings
sc()(invVerbosity=0, actionWarning=None, actionError=lambda: sys.exit(-10))

sc().header("SCout Logger")
sc().debug("Some debug message: 0xDEADBEEF")
sc().info("An info message")
sc().wwarning("Weak warning (does not support actions)")
sc().warning("This is a warning without defined action")
sc().error("Here the error action is defined as sys.exit(-10)")
