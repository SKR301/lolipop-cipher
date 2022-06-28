from Lolipop import Lolipop
from Lolipop import PadMatrix

if __name__ == '__main__':
    plainText = 'HELLO'
    cipher = Lolipop()
    crypt = cipher.encrypt(plainText)

    cipherText = crypt['cipherText']
    key = crypt['key']
    print()
    print('PlainText:', plainText)
    print('Crypted:', cipherText)
    print('Key: ', key)
    #     PadMatrix().printPadMatrix(cipher.createPadMatrix(key))
    #     print()

    cipher = Lolipop(key)
    decrypt = cipher.decrypt(cipherText)
    print('Decrypted:', decrypt)

        