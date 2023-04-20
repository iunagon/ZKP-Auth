from tinyec import registry
from Cryptodome.Cipher import AES
import hashlib
curve = registry.get_curve('brainpoolP256r1')
class LoginDec:
    def __hash_func(self,s:str):
        bytes_32 = hashlib.sha256(s.encode()).hexdigest()
        return bytes_32

    def __point_to_32bytes(self,point):
        sha = hashlib.sha256(int.to_bytes(point.x, 32, 'big'))
        sha.update(int.to_bytes(point.y, 32, 'big'))
        return sha.digest()
    def __decrypt_ECC(self,encryptedMsg,password):
        try:
            privKey = int(self.__hash_func(password), 16)
            while privKey >= curve.field.n:
                s = hex(privKey)
                privKey = int(hashlib.sha256(s.encode()).hexdigest(), 16)
            (ciphertext, nonce, authTag, ciphertextPubKey) = encryptedMsg
            sharedECCKey = privKey * ciphertextPubKey
            secretKey = self.__point_to_32bytes(sharedECCKey)
            aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
            plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
            return plaintext
        except:
            return None
    def decrypt(self,encrypted_msg,password):
        decryptedMsg = self.__decrypt_ECC(encrypted_msg,password)
        return decryptedMsg