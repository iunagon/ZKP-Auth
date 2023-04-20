from tinyec import registry
import hashlib
from PublicKeys import PublicKeys
class Register:
    __curve = registry.get_curve('brainpoolP256r1')
    def __hash_func(self,s:str):
        bytes_32 = hashlib.sha256(s.encode()).hexdigest()
        return bytes_32
    def __generate_public_key(self,password):

        privKey = int(self.__hash_func(password), 16)
        while privKey >= self.__curve.field.n:
            s = hex(privKey)
            privKey = int(hashlib.sha256(s.encode()).hexdigest(), 16)
        pubKey = privKey * self.__curve.g
        return pubKey
    def register(self,username,password):
        if password==None or password =="":
            return -1
        if PublicKeys.is_present(username):
            return -2
        pubKey = self.__generate_public_key(password)
        PublicKeys.set_public_key(username,pubKey)
        PublicKeys.display()
        return 1


