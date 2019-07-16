"""
SCout | Special Character Out

Copyright 2017-2019, Marcel Schmalzl (MSc)
This code is licensed under a MIT license
You should have received a copy of the MIT licence along with this program.
If not see:
* https://github.com/holzkohlengrill/SCout/blob/master/LICENSE
* https://opensource.org/licenses/MIT
"""

from pypiscout import SCout as sc


print("\n")

sc.header("Welcome to SCout!")
sc.debug("Some debug message: 0xDEADBEEF")
sc.info("An info message")
sc.wwarning("Weak warnings are supported")
sc.warning("This is a warning")
sc.error("An error occured")
