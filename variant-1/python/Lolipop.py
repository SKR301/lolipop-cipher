class Lolipop:
    def __init__(self, input='987654QPONM3REDCL2SFABK_TGHIJ#UVWXYZ'):
        if self.validatePadInput(input):
            self.padString = input
    
    # validate the input string for pad
    def validatePadInput(self, padInput):
        return True

    # create and return a pad matrix 
    def createPadMatrix(self, padString):
        print(f'creating Pad Matrix with: {padString}')

    # encrypt the input plaintext, returns cipher and key
    def encrypt(self, plainText):
        print(f'encrypting: {plainText}')
    
    # decrypt the input cipherText
    def decrypt(self, cipherText):
        print(f'decrypting: {cipherText}')

    # get row and col of input char 
    def getPosOfChar(self, char):
        print(f'finding position of {char}')

    # get char at input row and col 
    def getCharAtPost(self, pos):
        print(f'finding char at {pos}')

class Shift:
    # shift the row right given time 
    def shiftRight(self, rowNum, shiftCount, matrix):
        print(f'shifting row {rowNum} right by {shiftCount} in {matrix}')

    # shift the col down given time 
    def shiftDown(self, colNum, shiftCount, matrix):
        print(f'shifting col {colNum} down by {shiftCount} in {matrix}')

    # shift the row left given time 
    def shiftLeft(self, rowNum, shiftCount, matrix):
        print(f'shifting row {rowNum} left by {shiftCount} in {matrix}')

    # shift the col up given time 
    def shiftUp(self, colNum, shiftCount, matrix):
        print(f'shifting col {colNum} up by {shiftCount} in {matrix}')
