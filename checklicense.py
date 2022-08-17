from WrapGnupg import *
import os

class KeyLock:
  locks = []
  def KeyFile(self):
    return os.getcwd()+'\locks.txt'

  #add a key to the list
  def AddKey(self, key):
    self.locks.append(key)
    print(self.locks)
    with open(self.KeyFile() , 'w') as f:
      for i in self.locks:
        f.write('{}\n'.format(i))
      f.close

  #remove a key from the list
  def RemoveKey(self, key):
    self.locks.remove(key)
    #write file
    with open(self.KeyFile() , 'w') as f:
      for i in self.locks:
        f.write('{}\n'.format(i))
      f.close

#sender - encrypts file with VSG public key and signs with their own private key
#recipient - is VSG. We decrypt and verify signature.
#recipient then checks contents of the license file to see which license to check out.
#if ok, then return OK
#if not ok, return NO

SENDER_NAME = 'Benny Hill'
SENDER_EMAIL = 'benny.hill@bbc.com'
SENDER_COMMENT = ''
SENDER_PASSPHRASE = 'yakitysax'
MY_PRIVATE_PASSPHRASE = 'asdfasdf'

RECIPIENT_NAME = 'John Cleese'
RECIPIENT_EMAIL = 'cleesej@montypython.org'
RECIPIENT_COMMENT = 'funny, hahah'
RECIPIENT_PASSPHRASE = 'theCheeseSketch'

def checkoutMyKey(key):
    if key != '':
        fp = list_public_keys(key)
    if fp:
        loks = KeyLock()
        return loks.AddKey(fp.fingerprints)

def checkinMyKey(key):
    if key != '':
        fp = list_public_keys(key)
    if fp:
        loks = KeyLock()
        return loks.RemoveKey(fp.fingerprints)

def Main():
    checkoutMyKey(SENDER_EMAIL)

    #encrypt with recipient's public key and sign with my private passphrase
#    encrypt_and_sign_file(RECIPIENT_NAME, MY_PRIVATE_PASSPHRASE, 'C:\develop\python\gpg\TopSecretJoke3.txt')

    #as the recipient, decrypt with my private passphrase. Will not decrypt if sig not right.
#    verify_and_decrypt_file(RECIPIENT_PASSPHRASE, 'C:\develop\python\gpg\TopSecretJoke3.txt')



Main()