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
        cipher = Lolipop()

        # default pad matrix
        self.assertEqual(cipher.createPadMatrix('987654QPONM3REDCL2SFABK_TGHIJ#UVWXYZ'), [['9','8','7','6','5','4'],
                                                                                            ['Q','P','O','N','M','3'],
                                                                                            ['R','E','D','C','L','2'],
                                                                                            ['S','F','A','B','K','_'],
                                                                                            ['T','G','H','I','J','#'],
                                                                                            ['U','V','W','X','Y','Z']])

        # manual input pad string 
        self.assertEqual(cipher.createPadMatrix('S54ABK_XIJTGHL2#UEDCYZWQF9VPONM3R876'), [['S','5','4','A','B','K'],
                                                                                            ['_','X','I','J','T','G'],
                                                                                            ['H','L','2','#','U','E'],
                                                                                            ['D','C','Y','Z','W','Q'],
                                                                                            ['F','9','V','P','O','N'],
                                                                                            ['M','3','R','8','7','6']])
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
    
if __name__ == '__main__':
    unittest.main()