import unittest
from Markov import *


# tests.txt in file must be
# input_string : rule1^ rule2^... : answer ???????
# divided by newline
class TestMarkov(unittest.TestCase):

    def test(self):
        f = open("tests.txt")
        tests = f.readlines()
        for test_string in tests:
            test_string = test_string.split(" : ")
            self.assertEqual(markov(test_string[0], create_ruleset(test_string[1].split("^"))), test_string[2].strip())

