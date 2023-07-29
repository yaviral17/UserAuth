
import base64
from cryptography.fernet import Fernet
 

class AESEncryption:
    secrateKey = b"youKnowItsSecretKeyaviralyadav17"
    def encrypt(self,password):
        key = base64.b64encode(self.secrateKey)
        # Instance the Fernet class with the key
        fernet = Fernet(key)
        # then use the Fernet class instance
        # to encrypt the string string must
        # be encoded to byte string before encryption
        encMessage = fernet.encrypt(password.encode())
        return encMessage

    def decrypt(self,encryptedPassword):
        encryptedPassword = encryptedPassword.encode('utf-8')
        fernet = Fernet(base64.b64encode(self.secrateKey))
        decMessage = fernet.decrypt(encryptedPassword).decode()
        return decMessage


# print("Enter the password to be encrypted")
# password = input()
obj = AESEncryption()
# encryptedPassword = obj.encrypt(password)
# print("Encrypted Password is : ",encryptedPassword)
keyy = 'gAAAAABkpQrH46kTj5xVPaYMAjyHU1VnbkkkLIdK4tgPRXSTCJTFrfjRLloo-4D3XVykJ526xip8h7iN9VYETNekil_gnkbJ8Q=='
decryptedPassword = obj.decrypt(keyy)
print("Decrypted Password is : ",decryptedPassword)
