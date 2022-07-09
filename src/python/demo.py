from Lolipop import Lolipop

plainText = 'HELLO'

cipher = Lolipop()
crypt = cipher.encrypt(plainText)       # encryption => {cipher, key}
cipherText = crypt['cipherText']
key = crypt['key']

cipher = Lolipop(key)
decrypt = cipher.decrypt(cipherText)    # decryption => plaintext

# outputs
print('PlainText:', plainText)
print('Crypted:', cipherText)
print('Key: ', key)
print('Decrypted:', decrypt)

