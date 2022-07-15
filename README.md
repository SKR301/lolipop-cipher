# lolipop-cipher
A simple pen-paper cipher inspired by **OneTimePad** and **LC4** ciphers

## Usage
```python
from Lolipop import Lolipop

plainText = 'HELLO'

cipher = Lolipop()                      # using default key
crypt = cipher.encrypt(plainText)       # encryption => {cipher, key}
cipherText = crypt['cipherText']
key = crypt['key']

cipher = Lolipop(key)                   # Must use the key obtained from encryption
decrypt = cipher.decrypt(cipherText)    # decryption => plaintext

# outputs
print('PlainText:', plainText)
print('Crypted:', cipherText)
print('Key: ', key)
print('Decrypted:', decrypt)
```
![image](https://user-images.githubusercontent.com/47807051/178112295-a530e620-b30d-4e99-8dd6-49e57be517cf.png)


### Note:
*Cipher is vulnerable against* ***Plaintext-Ciphertext Pair Cryptanalysis***, *Please do not use it for sensitive data*
