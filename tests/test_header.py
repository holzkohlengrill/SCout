import unittest
from unittest import TestCase

import pypiscout.SCout as sc

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


class TestHeader(TestCase):
    def testSingleArg(self):
        print("Conducting test:", "testSingleArg")
        singleHeader = sc.Header.gen(TEXTSINGLE, symbol="/")
        print(singleHeader)
        self.assertMultiLineEqual(HEADEROUTPUT_EXPECTED, singleHeader)

    # def testMultiArg(self):
    #     """
    #     Test header multiline support (NOT IMPLEMENTED SO FAR)
    #     :return:
    #     """
    #     print("Conducting test:", "testMultiArg")
    #     singleHeader = sc.Header.gen(TEXTLIST, symbol="/")
    #     self.assertMultiLineEqual(HEADEROUTPUT_EXPECTED, singleHeader)


if __name__ == '__main__':
    unittest.main()
