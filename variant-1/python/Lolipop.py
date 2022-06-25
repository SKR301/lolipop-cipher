class Lolipop:
    def __init__(self, input='987654QPONM3REDCL2SFABK_TGHIJ#UVWXYZ'):
        input = input.upper()
        if self.validatePadInput(input):
            self.padString = input
    
    # preprocess input string for pad
    def preprocessPadInput(self, padInput):
        return padInput.upper().replace('0','#').replace('1','_')

    # validate the input string for pad
    def validatePadInput(self, padInput):
        if len(padInput) < 36:
            return False
        if len(padInput) > 36:
            return False
        if set('987654QPONM3REDCL2SFABK_TGHIJ#UVWXYZ') != set(padInput):
            return False
        
        return True

    # create and return a pad matrix 
    def createPadMatrix(self, padInput):
        padMatrix = []

        for a in range(6):
            temp = []
            for b in range(6):
                temp.append(padInput[a*6+b])
            padMatrix.append(temp)

        return padMatrix

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
    def shiftRow(self, rowNum, shiftCount, matrix):
        rowNum = rowNum % 6
        intercept = 6 - (shiftCount % 6)

        row = matrix[rowNum]
        matrix[rowNum] = row[intercept:] + row[0:intercept]
        return matrix

    # shift the col down given time 
    def shiftCol(self, colNum, shiftCount, matrix):
        print(f'shifting col {colNum} down by {shiftCount} in {matrix}')
