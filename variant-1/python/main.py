from Lolipop import Lolipop
from Lolipop import PadMatrix

if __name__ == '__main__':
    cipher = Lolipop()
    crypt = cipher.encrypt('MARTIN')

    cipherText = crypt['cipherText']
    key = crypt['key']

    print(cipherText)
    PadMatrix().printPadMatrix(key)