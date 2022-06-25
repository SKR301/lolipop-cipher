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

class PadMatrix:
    # shift the row right given time 
    def shiftRow(self, rowNum, shiftCount, matrix):
        rowNum = rowNum % 6
        intercept = 6 - (shiftCount % 6)

        row = matrix[rowNum]
        matrix[rowNum] = row[intercept:] + row[0:intercept]
        return matrix

    # shift the col down given time 
    def shiftCol(self, colNum, shiftCount, matrix):
        transMatrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
        self.shiftRow(colNum, shiftCount, transMatrix)
        matrix = [[row[i] for row in transMatrix] for i in range(len(transMatrix[0]))]
        return matrix
    
    # get row and col of input char 
    def getPosOfChar(self, char, matrix):
        for a in range(0, 6):
            for b in range(0, 6):
                if matrix[a][b] == char:
                    return (a,b)
        return (-1,-1)

    # get char at input row and col 
    def getCharAtPost(self, pos, matrix):
        print(f'finding char at {pos}')

