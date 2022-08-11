from WrapGnupg import *

#sender - encrypts file with VSG public key and signs with their own private key
#recipient - is VSG. We decrypt and verify signature.
#recipient then checks contents of the license file to see which license to check out. Also included - IP address, timestamp, username?
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

def Main():
    #encrypt with recipient's public key and sign with my private passphrase
    encrypt_and_sign_file(RECIPIENT_NAME, MY_PRIVATE_PASSPHRASE, 'C:\develop\python\gpg\TopSecretJoke3.txt')

    #as the recipient, decrypt with my private passphrase. Will not decrypt if sig not right.
    verify_and_decrypt_file(RECIPIENT_PASSPHRASE, 'C:\develop\python\gpg\TopSecretJoke3.txt')



Main()