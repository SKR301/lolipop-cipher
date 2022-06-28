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

    def test_dismantlePadMatrix(self):
        cipher = Lolipop()

        # dismantle default pad matrix
        self.assertEqual(cipher.dismantlePadMatrix([['9','8','7','6','5','4'],
                                                    ['Q','P','O','N','M','3'],
                                                    ['R','E','D','C','L','2'],
                                                    ['S','F','A','B','K','_'],
                                                    ['T','G','H','I','J','#'],
                                                    ['U','V','W','X','Y','Z']]), '987654QPONM3REDCL2SFABK_TGHIJ#UVWXYZ')

        # dismantle manual input pad string 
        self.assertEqual(cipher.dismantlePadMatrix([['S','5','4','A','B','K'],
                                                    ['_','X','I','J','T','G'],
                                                    ['H','L','2','#','U','E'],
                                                    ['D','C','Y','Z','W','Q'],
                                                    ['F','9','V','P','O','N'],
                                                    ['M','3','R','8','7','6']]), 'S54ABK_XIJTGHL2#UEDCYZWQF9VPONM3R876')

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
        shift = PadMatrix()
        padMatrix = [['9','8','7','6','5','4'],
                    ['Q','P','O','N','M','3'],
                    ['R','E','D','C','L','2'],
                    ['S','F','A','B','K','_'],
                    ['T','G','H','I','J','#'],
                    ['U','V','W','X','Y','Z']]

        # char not present 
        self.assertEqual(shift.getPosOfChar('*', padMatrix), (-1, -1))

        # char present 
        self.assertEqual(shift.getPosOfChar('A', padMatrix), (3,2))
    
    def test_getCharAtPost(self):
        shift = PadMatrix()
        padMatrix = [['9','8','7','6','5','4'],
                    ['Q','P','O','N','M','3'],
                    ['R','E','D','C','L','2'],
                    ['S','F','A','B','K','_'],
                    ['T','G','H','I','J','#'],
                    ['U','V','W','X','Y','Z']]

        # row < 0
        self.assertEqual(shift.getCharAtPos((-1,0), padMatrix), 'Input row value is -1. Must be between 0 and 6 [included]')

        # row > 6
        self.assertEqual(shift.getCharAtPos((7,0), padMatrix), 'Input row value is 7. Must be between 0 and 6 [included]')
        
        # col < 0
        self.assertEqual(shift.getCharAtPos((0,-1), padMatrix), 'Input column value is -1. Must be between 0 and 6 [included]')
        
        # col > 6
        self.assertEqual(shift.getCharAtPos((0,7), padMatrix), 'Input column value is 7. Must be between 0 and 6 [included]')
        
        # correct 
        self.assertEqual(shift.getCharAtPos((0,0), padMatrix), '9')

    def test_encrypt(self):
        # empty string
        cipher = Lolipop()
        self.assertEqual(cipher.encrypt(''), {'cipherText': '','key': '987654QPONM3REDCL2SFABK_TGHIJ#UVWXYZ'})

        # 5char test
        cipher = Lolipop()
        self.assertEqual(cipher.encrypt('HELLO'), {'cipherText': '9#QUT8','key': 'UEH637FOWMG_CL2QK#RVNBJZS8DIY49TPAX5'})

        # lowercase input
        cipher = Lolipop()
        self.assertEqual(cipher.encrypt('hello'), {'cipherText': '9#QUT8','key': 'UEH637FOWMG_CL2QK#RVNBJZS8DIY49TPAX5'})

    def test_decrypt(self):
        # empty string
        cipher = Lolipop()
        self.assertEqual(cipher.decrypt(''), '')

        # 5char test
        cipher = Lolipop('UEH637FOWMG_CL2QK#RVNBJZS8DIY49TPAX5')
        self.assertEqual(cipher.decrypt('9#QUT8'), 'HELLO')

        # lowercase input
        cipher = Lolipop('UEH637FOWMG_CL2QK#RVNBJZS8DIY49TPAX5')
        self.assertEqual(cipher.decrypt('9#qut8'), 'HELLO')
        
    def test_enc_dec(self):
        # single char test
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for plainText in alphabet:
            cipher = Lolipop()
            crypt = cipher.encrypt(plainText)

            cipherText = crypt['cipherText']
            key = crypt['key']

            cipher = Lolipop(key)
            decryptText = cipher.decrypt(cipherText)
            self.assertEqual(plainText, decryptText)
        
        # 5char test
        plainText = 'HELLO'
        cipher = Lolipop()
        crypt = cipher.encrypt(plainText)

        cipherText = crypt['cipherText']
        key = crypt['key']

        cipher = Lolipop(key)
        decryptText = cipher.decrypt(cipherText)
        self.assertEqual(plainText, decryptText)
        
        # 6char test
        plainText = 'HELLOS'
        cipher = Lolipop()
        crypt = cipher.encrypt(plainText)

        cipherText = crypt['cipherText']
        key = crypt['key']

        cipher = Lolipop(key)
        decryptText = cipher.decrypt(cipherText)
        self.assertEqual(plainText, decryptText)

        # 7char test 
        plainText = 'NIRVANA'
        cipher = Lolipop()
        crypt = cipher.encrypt(plainText)

        cipherText = crypt['cipherText']
        key = crypt['key']

        cipher = Lolipop(key)
        decryptText = cipher.decrypt(cipherText)
        self.assertEqual(plainText, decryptText)

        # 11char test 
        plainText = 'HELLOMARTIN'
        cipher = Lolipop()
        crypt = cipher.encrypt(plainText)

        cipherText = crypt['cipherText']
        key = crypt['key']

        cipher = Lolipop(key)
        decryptText = cipher.decrypt(cipherText)
        self.assertEqual(plainText, decryptText)

        # 12char test 
        plainText = 'HELLOSWORLDS'
        cipher = Lolipop()
        crypt = cipher.encrypt(plainText)

        cipherText = crypt['cipherText']
        key = crypt['key']

        cipher = Lolipop(key)
        decryptText = cipher.decrypt(cipherText)
        self.assertEqual(plainText, decryptText)

        # 13char test 
        plainText = 'QUADRUPLICATE'
        cipher = Lolipop()
        crypt = cipher.encrypt(plainText)

        cipherText = crypt['cipherText']
        key = crypt['key']

        cipher = Lolipop(key)
        decryptText = cipher.decrypt(cipherText)
        self.assertEqual(plainText, decryptText)

if __name__ == '__main__':
    unittest.main()