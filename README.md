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
![image](https://user-images.githubusercontent.com/47807051/176242627-0b543604-26bb-49a9-873b-3f32b810bc33.png)

### Note:
*Cipher is vulnerable against* ***Cryptanalysis***, *Please do not use it for sensitive data*
