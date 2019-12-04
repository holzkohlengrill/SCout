"""
SCout | Special Character Out

Copyright 2017-2019, Marcel Schmalzl (MSc)
This code is licensed under a MIT license
You should have received a copy of the MIT licence along with this program.
If not see:
* https://github.com/holzkohlengrill/SCout/blob/master/LICENSE
* https://opensource.org/licenses/MIT
"""

import unittest
from unittest import TestCase

from pypiscout.SCout_Logger import Logger as sc

aWarning = None
aErr = None

class TestLoggerVerbosity(TestCase):
    def testIntNormal1(self):
        """
        Check if no exception appears - normal case
        """
        sc()(int(0), actionWarning=aWarning, actionError=aErr)

    def testIntNormal2(self):
        """
        Check if no exception appears - normal case
        """
        sc()(int(-555), actionWarning=aWarning, actionError=aErr)

    def testIntNormal3(self):
        """
        Check if no exception appears - normal case
        """
        sc()(int(-1), actionWarning=aWarning, actionError=aErr)

    def testIntNormal4(self):
        """
        Check if no exception appears - normal case
        """
        sc()(int(42), actionWarning=aWarning, actionError=aErr)

    def testIntNormal5(self):
        """
        Check if no exception appears - normal case
        """
        sc()(int(2), actionWarning=aWarning, actionError=aErr)

    def testStrNormal(self):
        """
        Check if no exception appears - normal case
        """
        sc()("0", actionWarning=aWarning, actionError=aErr)

    def testStrNegNormal(self):
        """
        Check if no exception appears - normal case
        """
        sc()("-42", actionWarning=aWarning, actionError=aErr)

    def testStrInvalidStr1(self):
        """
        Check if no exception appears - invalid case
        """
        with self.assertRaises(ValueError):
            sc()("--42", actionWarning=aWarning, actionError=aErr)

    def testStrInvalidStr2(self):
        """
        Check if no exception appears - invalid case
        """
        with self.assertRaises(ValueError):
            sc()(str("1aaaf42"), actionWarning=aWarning, actionError=aErr)

    def testStrInvalidStr3(self):
        """
        Check if no exception appears - invalid case
        """
        with self.assertRaises(ValueError):
            sc()("-42a", actionWarning=aWarning, actionError=aErr)


if __name__ == '__main__':
    unittest.main()
