import copy
import math

class Lolipop:
    def __init__(self, input='987654QPONM3REDCL2SFABK_TGHIJ#UVWXYZ'):
        input = input.upper()
        self.padString = ''
        if self.validatePadInput(input):
            self.padString = input
        
        self.padMatrix = self.createPadMatrix(self.padString)
    
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
                temp.append(padInput[a * 6 + b])
            padMatrix.append(temp)

        return padMatrix

    # create dismantled string from pad matrix 
    def dismantlePadMatrix(self, matrix):
        dismantledStr = ''
        for row in matrix:
            for ch in row:
                dismantledStr += ch
        return dismantledStr

    # encrypt the input plaintext, returns cipher and key
    def encrypt(self, plainText):
        if len(plainText) == 0:
            return {'cipherText':'', 'key': self.dismantlePadMatrix(self.padMatrix)}

        plainText = 'A'+plainText.upper()+'A'
        cipherText = ''
        
        currPos = PadMatrix().getPosOfChar(plainText[0], copy.deepcopy(self.padMatrix))
        for a in range(1, len(plainText)):
            currChar = plainText[a]
            ind = (a-1)%6
            charPos = PadMatrix().getPosOfChar(currChar, copy.deepcopy(self.padMatrix))
            relPos = ((charPos[0] - currPos[0]) % 6, (charPos[1] - currPos[1]) % 6)
            
            self.padMatrix = PadMatrix().shiftCol(ind, relPos[0], copy.deepcopy(self.padMatrix))
            self.padMatrix = PadMatrix().shiftRow(ind, relPos[1], copy.deepcopy(self.padMatrix))

            cipherText += PadMatrix().getCharAtPos(relPos, copy.deepcopy(self.padMatrix))
            currPos = PadMatrix().getPosOfChar(currChar, copy.deepcopy(self.padMatrix))

        key = self.dismantlePadMatrix(self.padMatrix)
        cipherText = cipherText.ljust(math.ceil(len(cipherText)/6)*6, '$')

        return {'cipherText': cipherText, 'key': key}
    
    # decrypt the input cipherText
    def decrypt(self, cipherText):
        if len(cipherText) == 0:
            return ''

        cipherText = cipherText[::-1]

        decryptText = 'A'
        for a in range(0, len(cipherText)):
            if cipherText[a] == '$':
                continue

            currChar = cipherText[a]
            ind = (5-a)%6
            charPos = PadMatrix().getPosOfChar(currChar, copy.deepcopy(self.padMatrix))

            self.padMatrix = PadMatrix().shiftRow(ind, -charPos[1], copy.deepcopy(self.padMatrix))
            self.padMatrix = PadMatrix().shiftCol(ind, -charPos[0], copy.deepcopy(self.padMatrix))

            currPos = PadMatrix().getPosOfChar(decryptText[len(decryptText)-1], copy.deepcopy(self.padMatrix))
            relPos = (currPos[0] - charPos[0])%6, (currPos[1] - charPos[1])%6

            # print(currChar, charPos, currPos, relPos, decryptText)
            # PadMatrix().printPadMatrix(copy.deepcopy(self.padMatrix))

            decryptText += PadMatrix().getCharAtPos(relPos, copy.deepcopy(self.padMatrix))
        return decryptText[1:-1]

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
    def getCharAtPos(self, pos, matrix):
        if pos[0] < 0 or pos[0] > 6:
            return f'Input row value is {pos[0]}. Must be between 0 and 6 [included]'
        if pos[1] < 0 or pos[1] > 6:
            return f'Input column value is {pos[1]}. Must be between 0 and 6 [included]'

        return matrix[pos[0]][pos[1]]

    # print the matrix 
    def printPadMatrix(self, matrix):
        for row in matrix:
            print(row)
        print()
       