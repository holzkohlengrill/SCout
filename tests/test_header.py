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
from pypiscout.SCout_Logger import Logger as sc

TEXTLIST = [
    "Lorem ipsum dolor sit amet, consetetur sadipscing elitr,",
    " sed diam nonumy eirmod tempor invidunt ut labore et dolore magna",
    " aliquyam erat, sed diam voluptua.",
    " At vero eos et accusam et justo duo dolores et ea rebum.",
    " Stet clita kasd gubergren, no sea takimata "
]
TEXTSINGLE = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr,"

##################

HEADEROUTPUT_EXPECTED = """////////////////////////////////////////////////////////////////
/// Lorem ipsum dolor sit amet, consetetur sadipscing elitr, ///
////////////////////////////////////////////////////////////////
"""     # This newline is important
HEADEROUTPUT_MULTILINE_EXPECTED = [
    "Lorem ipsum dolor sit amet, consetetur sadipscing elitr,",
    " sed diam nonumy eirmod tempor invidunt ut labore et dolore magna",
    " aliquyam erat, sed diam voluptua.",
    " At vero eos et accusam et justo duo dolores et ea rebum.",
    " Stet clita kasd gubergren, no sea takimata "
]


class TestHeaderSimple(TestCase):
    def testSingleArg(self):
        singleHeader = sc_simple.Header.gen(TEXTSINGLE, symbol="/")
        print(singleHeader)
        self.assertMultiLineEqual(HEADEROUTPUT_EXPECTED, singleHeader)

    # def testMultiArg(self):
    #     """
    #     Test header multiline support (NOT IMPLEMENTED SO FAR)
    #     :return:
    #     """
    #     print("Conducting test:", "testMultiArg")
    #     singleHeader = sc_simple.Header.gen(TEXTLIST, symbol="/")
    #     self.assertMultiLineEqual(HEADEROUTPUT_EXPECTED, singleHeader)


class TestHeaderLogger(TestCase):
    def testSingleArg(self):
        singleHeader = sc().header(TEXTSINGLE, symbol="/", disableColour=True)
        self.assertMultiLineEqual(HEADEROUTPUT_EXPECTED, singleHeader)


if __name__ == '__main__':
    unittest.main()
