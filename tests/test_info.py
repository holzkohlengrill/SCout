import unittest
from unittest import TestCase

import pypiscout.SCout as sc

TEXTLIST = [
    "Lorem ipsum dolor sit amet, consetetur sadipscing elitr,",
    "sed diam nonumy eirmod tempor invidunt ut labore et dolore magna",
    "aliquyam erat, sed diam voluptua.",
    "At vero eos et accusam et justo duo dolores et ea rebum.",
    "Stet clita kasd gubergren, no sea takimata "
]
TEXTSINGLE = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr,"

##################

INFOOUTPUT_EXPECTED =  "   (info) :  Lorem ipsum dolor sit amet, consetetur sadipscing elitr,"
MULTIOUTPUT_EXPECTED = "   (info) :  Lorem ipsum dolor sit amet, consetetur sadipscing elitr, \
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna \
aliquyam erat, sed diam voluptua. \
At vero eos et accusam et justo duo dolores et ea rebum. \
Stet clita kasd gubergren, no sea takimata "


class TestInfo(TestCase):
    def testSingleArg(self):
        print("Conducting test:", "testSingleArg")
        singleInfo= sc.info(TEXTSINGLE, disableColour=True)
        self.assertEqual(INFOOUTPUT_EXPECTED, singleInfo)

    def testMultiArg(self):
        print("Conducting test:", "testMultiArg")
        multiInfo = sc.info(*TEXTLIST, disableColour=True)
        self.assertMultiLineEqual(MULTIOUTPUT_EXPECTED, multiInfo)
        print(MULTIOUTPUT_EXPECTED)
        print("Second `print()` was expected output")


if __name__ == '__main__':
    unittest.main()
