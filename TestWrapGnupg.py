import unittest
import os
from WrapGnupg import *

SENDER_NAME = 'Marv Drake'
SENDER_EMAIL = 'blah11@blah.com'
SENDER_COMMENT = 'comment for '+SENDER_NAME
SENDER_PASSPHRASE = 'imaG00Done'

RECIPIENT_NAME = 'Barfy Dog'
RECIPIENT_EMAIL = 'barfy@blah.com'
RECIPIENT_COMMENT = 'comment for '+RECIPIENT_NAME
RECIPIENT_PASSPHRASE = 'imaG00Done'

IMPORT_KEY_FILE = 'C:/develop/python/vsgLicense/foo2.txt'
EXPORT_KEY_FILE = 'C:/develop/python/vsgLicense/keyout.txt'
PLAINTEXT_FILE = 'C:/develop/python/vsgLicense/plaintext.txt'
ENCRYPTED_FILE = 'C:/develop/python/vsgLicense/plaintext2.txt'


class MyTestCase(unittest.TestCase):
    def test_export_key(self):
        self.assertEqual(export_key(SENDER_EMAIL, SENDER_PASSPHRASE, EXPORT_KEY_FILE).__len__() > 0, True)

    def test_import_key(self):
        self.assertEqual(import_key(SENDER_PASSPHRASE, IMPORT_KEY_FILE).__len__() > 0, True)  # add assertion here

    def test_list_public_keys(self):
        self.assertEqual(list_public_keys(RECIPIENT_EMAIL).__len__() > 0, True)  # add assertion here

    def test_delete_public_key(self):
        self.assertEqual(delete_public_key(RECIPIENT_EMAIL, SENDER_PASSPHRASE), True)  # add assertion here

    def test_list_private_keys(self, SENDER_EMAIL):
        self.assertEqual(list_private_keys().__len__() >0, True)  # add assertion here

    def test_encrypt_file(self):
        f = open(PLAINTEXT_FILE, "w")
        f.write("This is a bunch of plain text to use for testing")
        f.close()
        self.assertEqual(encrypt_file(RECIPIENT_EMAIL, PLAINTEXT_FILE).ok, True)  # add assertion here
        os.remove(PLAINTEXT_FILE)

    def test_encrypt_and_sign_file(self):
        self.assertEqual(encrypt_and_sign_file(SENDER_EMAIL, SENDER_PASSPHRASE, 'C:/develop/python/gpg/plaintext2.txt').ok, True)  # add assertion here

    def test_decrypt_file(self):
        self.assertEqual(decrypt_file(SENDER_PASSPHRASE, ENCRYPTED_FILE).ok, True)  # add assertion here

    def test_verify_and_decrypt_file(self):
        self.assertEqual(verify_and_decrypt_file(SENDER_PASSPHRASE, ENCRYPTED_FILE).ok, True)  # add assertion here

    def test_encrypt_txt(self):
        self.assertEqual(encrypt_txt('asdfasdfasdfasdf', RECIPIENT_EMAIL).__len__() > 0, True)  # add assertion here

    # def test_decrypt_txt(self):
    #     self.assertEqual(decrypt_txt(input_data, PASS_PHRASE), True)  # add assertion here


if __name__ == '__main__':
    initialize(SENDER_NAME, SENDER_EMAIL, SENDER_PASSPHRASE, SENDER_COMMENT)
    initialize(RECIPIENT_NAME, RECIPIENT_EMAIL, RECIPIENT_PASSPHRASE, RECIPIENT_COMMENT)

    unittest.main()

    #TBD
    #update public key
    #backup keyring
    #encrypt text
    #decrypt text
