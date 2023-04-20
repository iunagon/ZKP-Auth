import pickle
class PublicKeysList:
    file=open('PKfile', 'rb')
    __d= pickle.load(file)
    file.close()
    def is_present(self,username):
        if username not in PublicKeysList.__d:
            return False
        else:
            return True

    def get_public_key(self,username):
        if username in PublicKeysList.__d:
            return PublicKeysList.__d[username]
        else:
            return False

    def set_public_key(self,username,public_key):
        if username not in PublicKeysList.__d:
            PublicKeysList.__d[username]=public_key
        else:
            return -1
        myFile = open('PKfile', 'wb')
        pickle.dump(self.__d, myFile)
        myFile.close()
    def reset_public_key(self,username,public_key):
        if username in PublicKeysList.__d:
            PublicKeysList.__d[username]=public_key
        else:
            return -1
    def empty(self):
        myFile = open('PKfile', 'wb')
        pickle.dump({}, myFile)
        myFile.close()
    def display(self):
        for i in PublicKeysList.__d:
            print(i,PublicKeysList.__d[i])


PublicKeys= PublicKeysList()
#PublicKeys.empty()


