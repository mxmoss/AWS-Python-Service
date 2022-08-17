from WrapGnupg import *
import os

class KeyLock:
    locks = []
    def KeyFile(self):
        return os.getcwd()+'\locks.txt'

    def writeLocks(self):
        with open(self.KeyFile() , 'w') as f:
            for i in self.locks:
                f.write('{}\n'.format(i))
            f.close

    #add a key to the list
    def AddKey(self, key):
        self.locks.append(key)
        self.writeLocks()
        return True

    #remove a key from the list
    def RemoveKey(self, key):
        self.locks.remove(key)
        self.writeLocks()
        return True

#sender - encrypts file with VSG public key and signs with their own private key
#recipient - is VSG. We decrypt and verify signature.
#recipient then checks contents of the license file to see which license to check out.
#if ok, then return OK
#if not ok, return NO

# eg:  checkoutMyKey(SENDER_EMAIL, 'checkout')
def checkoutMyKey(key, action):
    if key != '':
        fp = list_public_keys(key)
    if fp:
        loks = KeyLock()
        if action == 'checkout':
            return loks.AddKey(fp.fingerprints)
        if action == 'checkin':
            return loks.RemoveKey(fp.fingerprints)
    return False

    SENDER_NAME = 'Benny Hill'
    SENDER_EMAIL = 'benny.hill@bbc.com'
    SENDER_COMMENT = ''
    SENDER_PASSPHRASE = 'yakitysax'
    MY_PRIVATE_PASSPHRASE = 'asdfasdf'

    RECIPIENT_NAME = 'John Cleese'
    RECIPIENT_EMAIL = 'cleesej@montypython.org'
    RECIPIENT_COMMENT = 'funny, hahah'
    RECIPIENT_PASSPHRASE = 'theCheeseSketch'
    #encrypt with recipient's public key and sign with my private passphrase
#    encrypt_and_sign_file(RECIPIENT_NAME, MY_PRIVATE_PASSPHRASE, 'C:\develop\python\gpg\TopSecretJoke3.txt')

    #as the recipient, decrypt with my private passphrase. Will not decrypt if sig not right.
#    verify_and_decrypt_file(RECIPIENT_PASSPHRASE, 'C:\develop\python\gpg\TopSecretJoke3.txt')
