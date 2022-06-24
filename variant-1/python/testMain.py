import unittest
from Lolipop import Lolipop

class TestLolipop(unittest.TestCase):
    def test_validatePadInput(self):
        # size<36
        # size = 36 but value replaced 
        # no input 
        # default input passed 
        # correct input 
        print()

    def test_createPadMatrix(self):
        # default pad matrix
        # manual input pad string 
        print()

    def test_shiftRight(self):
        # row < 0
        # row > 6
        # shift count < 0
        # correct amount 
        print()

    def test_shiftDown(self):
        # col < 0
        # col > 6
        # shift count < 0
        # correct amount 
        print()

    def test_shiftLeft(self):
        # row < 0
        # row > 6
        # shift count < 0
        # correct amount 
        print()

    def test_shiftUp(self):
        # col < 0
        # col > 6
        # shift count < 0
        # correct amount 
        print()

    def test_encrypt(self):
        # empty string
        # size = 1
        # size > 36
        # same character repeated 10 times 
        # same pair repeated 10 times 
        print()