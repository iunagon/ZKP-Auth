from tinyec import registry
from Cryptodome.Cipher import AES
import hashlib, secrets
from random import randint
from PublicKeys import PublicKeys
curve = registry.get_curve('brainpoolP256r1')
class LoginEnc:
    def __init__(self):
        self.__random_string = self.__generate_randomstring(randint(90000,100000))
    def __point_to_32bytes(self,point):
        sha = hashlib.sha256(int.to_bytes(point.x, 32, 'big'))
        sha.update(int.to_bytes(point.y, 32, 'big'))
        return sha.digest()
    def __encrypt_ECC(self,msg, pubKey):
        ciphertextPrivKey = secrets.randbelow(curve.field.n)
        sharedECCKey = ciphertextPrivKey * pubKey
        secretKey = self.__point_to_32bytes(sharedECCKey)
        aesCipher = AES.new(secretKey, AES.MODE_GCM)
        ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
        nonce=aesCipher.nonce
        ciphertextPubKey = ciphertextPrivKey * curve.g
        return (ciphertext, nonce, authTag, ciphertextPubKey)
    def __generate_randomstring(self,length):
        random_string = ""
        for i in range(length):
            random_string += chr(randint(1, 256))
        random_string = bytes(random_string, 'utf-8')
        return random_string
    def get_encrypt(self,username):
        pubKey = PublicKeys.get_public_key(username)
        encryptedMsg = self.__encrypt_ECC(self.__random_string, pubKey)

        return (encryptedMsg)
    def isValid(self,string):
        return string == self.__random_string

