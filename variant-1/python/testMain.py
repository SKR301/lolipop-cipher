import unittest
import copy
from Lolipop import Lolipop
from Lolipop import PadMatrix

class TestLolipop(unittest.TestCase):
    def test_preprocessPadInput(self):
        cipher = Lolipop()

        # random lowercase with digit[0,1] and special char 
        self.assertTrue(cipher.preprocessPadInput('asd^#%1203#$asd%'), 'ASD^#%_2#3#$ASD%')

        # random uppercase with digit[0,1] and special char 
        self.assertTrue(cipher.preprocessPadInput('ASD^#%1203#$ASD%'), 'ASD^#%_2#3#$ASD%')

        # random default input string
        self.assertTrue(cipher.preprocessPadInput('987654QPONM3REDCL2SFABK_TGHIJ#UVWXYZ'), '987654QPONM3REDCL2SFABK_TGHIJ#UVWXYZ')

    def test_validatePadInput(self):
        cipher = Lolipop()
        
        # size<36
        self.assertFalse(cipher.validatePadInput('ASD'))

        # size>36
        self.assertFalse(cipher.validatePadInput('987654QPONM3REDCL2SFABK_TGHIJ#UVWXYZ^%'))

        # size = 36 but value replaced 
        self.assertFalse(cipher.validatePadInput('987654AAAAAAAAAAAAAAAAA_AAAAA#AAAAAA'))

        # default input passed 
        self.assertTrue(cipher.validatePadInput('987654QPONM3REDCL2SFABK_TGHIJ#UVWXYZ'))

        # correct input 
        self.assertTrue(cipher.validatePadInput('TGHIXYZ8765EDCL2SFABK_4QPJ#UVW9ONM3R'))

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

    def test_shiftRow(self):
        shift = PadMatrix()
        padMatrix = [['9','8','7','6','5','4'],
                    ['Q','P','O','N','M','3'],
                    ['R','E','D','C','L','2'],
                    ['S','F','A','B','K','_'],
                    ['T','G','H','I','J','#'],
                    ['U','V','W','X','Y','Z']]

        # row < 0
        self.assertEqual(shift.shiftRow(-2, 2, copy.deepcopy(padMatrix)), [['9','8','7','6','5','4'],
                                                                            ['Q','P','O','N','M','3'],
                                                                            ['R','E','D','C','L','2'],
                                                                            ['S','F','A','B','K','_'],
                                                                            ['J','#','T','G','H','I'],
                                                                            ['U','V','W','X','Y','Z']])

        # row > 6
        self.assertEqual(shift.shiftRow(10, 2, copy.deepcopy(padMatrix)), [['9','8','7','6','5','4'],
                                                                            ['Q','P','O','N','M','3'],
                                                                            ['R','E','D','C','L','2'],
                                                                            ['S','F','A','B','K','_'],
                                                                            ['J','#','T','G','H','I'],
                                                                            ['U','V','W','X','Y','Z']])

        # shift count < 0
        self.assertEqual(shift.shiftRow(0, -2, copy.deepcopy(padMatrix)), [['7','6','5','4','9','8'],
                                                                            ['Q','P','O','N','M','3'],
                                                                            ['R','E','D','C','L','2'],
                                                                            ['S','F','A','B','K','_'],
                                                                            ['T','G','H','I','J','#'],
                                                                            ['U','V','W','X','Y','Z']])

        # shift count > 6
        self.assertEqual(shift.shiftRow(0, 10, copy.deepcopy(padMatrix)), [['7','6','5','4','9','8'],
                                                                            ['Q','P','O','N','M','3'],
                                                                            ['R','E','D','C','L','2'],
                                                                            ['S','F','A','B','K','_'],
                                                                            ['T','G','H','I','J','#'],
                                                                            ['U','V','W','X','Y','Z']])

        # correct amount 
        self.assertEqual(shift.shiftRow(3, 3, copy.deepcopy(padMatrix)), [['9','8','7','6','5','4'],
                                                                            ['Q','P','O','N','M','3'],
                                                                            ['R','E','D','C','L','2'],
                                                                            ['B','K','_','S','F','A'],
                                                                            ['T','G','H','I','J','#'],
                                                                            ['U','V','W','X','Y','Z']])

    def test_shiftDown(self):
        shift = PadMatrix()
        padMatrix = [['9','8','7','6','5','4'],
                    ['Q','P','O','N','M','3'],
                    ['R','E','D','C','L','2'],
                    ['S','F','A','B','K','_'],
                    ['T','G','H','I','J','#'],
                    ['U','V','W','X','Y','Z']]

        # col < 0
        self.assertEqual(shift.shiftCol(-2, 2, copy.deepcopy(padMatrix)), [['9','8','7','6','J','4'],
                                                                            ['Q','P','O','N','Y','3'],
                                                                            ['R','E','D','C','5','2'],
                                                                            ['S','F','A','B','M','_'],
                                                                            ['T','G','H','I','L','#'],
                                                                            ['U','V','W','X','K','Z']])

        # col > 6
        self.assertEqual(shift.shiftCol(10, 2, copy.deepcopy(padMatrix)), [['9','8','7','6','J','4'],
                                                                            ['Q','P','O','N','Y','3'],
                                                                            ['R','E','D','C','5','2'],
                                                                            ['S','F','A','B','M','_'],
                                                                            ['T','G','H','I','L','#'],
                                                                            ['U','V','W','X','K','Z']])

        # shift count < 0
        self.assertEqual(shift.shiftCol(0, -2, copy.deepcopy(padMatrix)), [['R','8','7','6','5','4'],
                                                                            ['S','P','O','N','M','3'],
                                                                            ['T','E','D','C','L','2'],
                                                                            ['U','F','A','B','K','_'],
                                                                            ['9','G','H','I','J','#'],
                                                                            ['Q','V','W','X','Y','Z']])


        # shift count > 0
        self.assertEqual(shift.shiftCol(0, 10, copy.deepcopy(padMatrix)), [['R','8','7','6','5','4'],
                                                                            ['S','P','O','N','M','3'],
                                                                            ['T','E','D','C','L','2'],
                                                                            ['U','F','A','B','K','_'],
                                                                            ['9','G','H','I','J','#'],
                                                                            ['Q','V','W','X','Y','Z']])

        # correct amount 
        self.assertEqual(shift.shiftCol(3, 3, copy.deepcopy(padMatrix)), [['9','8','7','B','5','4'],
                                                                            ['Q','P','O','I','M','3'],
                                                                            ['R','E','D','X','L','2'],
                                                                            ['S','F','A','6','K','_'],
                                                                            ['T','G','H','N','J','#'],
                                                                            ['U','V','W','C','Y','Z']])

    def test_getPosOfChar(self):
        # char not present 
        # char present 
        print()
    
    def test_getCharAtPost(self):
        # row < 0
        # row > 6
        # col < 0
        # col > 6
        # correct 
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