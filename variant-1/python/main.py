from Lolipop import Lolipop
from Lolipop import PadMatrix

if __name__ == '__main__':
    cipher = Lolipop()
    crypt = cipher.encrypt('HELLO')

    cipherText = crypt['cipherText']
    key = crypt['key']

    print('Crypted:', cipherText)
    print('Key: ', key)
    
    # print()

    # cipher = Lolipop(key)
    # plainText = cipher.decrypt(cipherText)
    # print('Decrypted:', plainText)