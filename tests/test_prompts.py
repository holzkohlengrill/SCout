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

import pypiscout.SCout as sc_simple
from pypiscout.SCout import __ALIGNMENT

TEXTLIST = [
    "Lorem ipsum dolor sit amet, consetetur sadipscing elitr,",
    "sed diam nonumy eirmod tempor invidunt ut labore et dolore magna",
    "aliquyam erat, sed diam voluptua.",
    "At vero eos et accusam et justo duo dolores et ea rebum.",
    "Stet clita kasd gubergren, no sea takimata "
]
TEXTSINGLE = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr,"

##################
DEBUG = "(debug) :".rjust(__ALIGNMENT)
INFO = "(info) :".rjust(__ALIGNMENT)
WARNING = "(warning) :".rjust(__ALIGNMENT)
WWARNING = "(weak warning) :".rjust(__ALIGNMENT)
ERROR = "(error) :".rjust(__ALIGNMENT)

INFOOUTPUT_EXPECTED = " Lorem ipsum dolor sit amet, consetetur sadipscing elitr,"
MULTIOUTPUT_EXPECTED = " Lorem ipsum dolor sit amet, consetetur sadipscing elitr, \
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna \
aliquyam erat, sed diam voluptua. \
At vero eos et accusam et justo duo dolores et ea rebum. \
Stet clita kasd gubergren, no sea takimata "


class TestDebug(TestCase):
    def setUp(self):
        self.PREFIX = DEBUG

    def testSingleArg(self):
        print("Conducting test:", "testSingleArg")
        singleInfo = sc_simple.debug(TEXTSINGLE, disableColour=True)
        self.assertEqual(self.PREFIX + INFOOUTPUT_EXPECTED, singleInfo)

    def testMultiArg(self):
        print("Conducting test:", "testMultiArg")
        multiInfo = sc_simple.debug(*TEXTLIST, disableColour=True)
        self.assertMultiLineEqual(self.PREFIX + MULTIOUTPUT_EXPECTED, multiInfo)
        print(self.PREFIX + MULTIOUTPUT_EXPECTED)
        print("Second `print()` was expected output")


class TestInfo(TestCase):
    def setUp(self):
        self.PREFIX = INFO

    def testSingleArg(self):
        print("Conducting test:", "testSingleArg")
        singleInfo = sc_simple.info(TEXTSINGLE, disableColour=True)
        self.assertEqual(self.PREFIX + INFOOUTPUT_EXPECTED, singleInfo)

    def testMultiArg(self):
        print("Conducting test:", "testMultiArg")
        multiInfo = sc_simple.info(*TEXTLIST, disableColour=True)
        self.assertMultiLineEqual(self.PREFIX + MULTIOUTPUT_EXPECTED, multiInfo)
        print(self.PREFIX + MULTIOUTPUT_EXPECTED)
        print("Second `print()` was expected output")


class TestWarning(TestCase):
    def setUp(self):
        self.PREFIX = WARNING

    def testSingleArg(self):
        print("Conducting test:", "testSingleArg")
        singleInfo = sc_simple.warning(TEXTSINGLE, disableColour=True)
        self.assertEqual(self.PREFIX + INFOOUTPUT_EXPECTED, singleInfo)

    def testMultiArg(self):
        print("Conducting test:", "testMultiArg")
        multiInfo = sc_simple.warning(*TEXTLIST, disableColour=True)
        self.assertMultiLineEqual(self.PREFIX + MULTIOUTPUT_EXPECTED, multiInfo)
        print(self.PREFIX + MULTIOUTPUT_EXPECTED)
        print("Second `print()` was expected output")


class TestWWarning(TestCase):
    def setUp(self):
        self.PREFIX = WWARNING

    def testSingleArg(self):
        print("Conducting test:", "testSingleArg")
        singleInfo = sc_simple.wwarning(TEXTSINGLE, disableColour=True)
        self.assertEqual(self.PREFIX + INFOOUTPUT_EXPECTED, singleInfo)

    def testMultiArg(self):
        print("Conducting test:", "testMultiArg")
        multiInfo = sc_simple.wwarning(*TEXTLIST, disableColour=True)
        self.assertMultiLineEqual(self.PREFIX + MULTIOUTPUT_EXPECTED, multiInfo)
        print(self.PREFIX + MULTIOUTPUT_EXPECTED)
        print("Second `print()` was expected output")


class TestError(TestCase):
    def setUp(self):
        self.PREFIX = ERROR

    def testSingleArg(self):
        print("Conducting test:", "testSingleArg")
        singleInfo = sc_simple.error(TEXTSINGLE, disableColour=True)
        self.assertEqual(self.PREFIX + INFOOUTPUT_EXPECTED, singleInfo)

    def testMultiArg(self):
        print("Conducting test:", "testMultiArg")
        multiInfo = sc_simple.error(*TEXTLIST, disableColour=True)
        self.assertMultiLineEqual(self.PREFIX + MULTIOUTPUT_EXPECTED, multiInfo)
        print(self.PREFIX + MULTIOUTPUT_EXPECTED)
        print("Second `print()` was expected output")


if __name__ == '__main__':
    unittest.main()
