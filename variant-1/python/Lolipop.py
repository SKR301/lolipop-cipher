class Lolipop:
    def __init__(self, input='987654QPONM3REDCL2SFABK_TGHIJ#UVWXYZ'):
        self.padString = input
        self.createPadMatrix()
    
    # create and return a pad matrix 
    def createPadMatrix(self):
        print(f'creating Pad Matrix with: {self.padString}')

    # encrypt the input plaintext
    def encrypt(self, plainText):
        print(f'encrypting: {plainText}')
    
    # decrypt the input cipherText
    def decrypt(self, cipherText):
        print(f'decrypting: {cipherText}')

    # shift the row right given time 
    def shiftRight(self, rowNum, shiftCount):
        print(f'shifting row {rowNum} right by {shiftCount}')

    # shift the col down given time 
    def shiftDown(self, colNum, shiftCount):
        print(f'shifting col {colNum} down by {shiftCount}')

    # shift the row left given time 
    def shiftLeft(self, rowNum, shiftCount):
        print(f'shifting row {rowNum} left by {shiftCount}')

    # shift the col up given time 
    def shiftUp(self, colNum, shiftCount):
        print(f'shifting col {colNum} up by {shiftCount}')

    # get row and col of input char 
    def getPosOfChar(self, char):
        print(f'finding position of {char}')

    # get char at input row and col 
    def getCharAtPost(self, pos):
        print(f'finding char at {pos}')
