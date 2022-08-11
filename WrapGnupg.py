import gnupg

GNUPG_EXE = 'C:/develop/python/gpg/gpg.exe'
gpg = gnupg.GPG(gpgbinary=GNUPG_EXE,  verbose=True)

def initialize(name_txt, email_txt, passphrase_txt, comment_txt):
    # Uses for the key. Can be things like 'cert,sign' or 'cert' or 'cert,auth'.
    KEY_TYPE = 'RSA'
    KEY_LENGTH = 4096 #8192
    SUBKEY_TYPE = 'RSA'
    SUBKEY_LENGTH = 4096
    KEY_USAGE = 'cert'
    # SUBKEY_USAGE = 'sign'
    # KEYSERVER = None
    # Expiration date for the new key. To use the default expiration of one year, set to None.
    # EXPIRE_DATE = None
    EXPIRE_DATE = '2029-12-31'

    key_input = gpg.gen_key_input(
                                   name_email=email_txt,
                                   passphrase=passphrase_txt,
                                   name_real = name_txt,
                                   name_comment=comment_txt,
                                   key_type = KEY_TYPE,
                                   key_length = KEY_LENGTH,
                                   subkey_type=SUBKEY_TYPE,
                                   subkey_length=SUBKEY_LENGTH,
                                   expire_date=EXPIRE_DATE)

    key = gpg.gen_key(key_input)
    return

def export_key(keyname, passphrase_txt, file_out):
    with open(file_out, 'wb') as f:
        export_result = gpg.export_keys(keyname, passphrase=passphrase_txt, armor=True)
        f.write(bytes (export_result, 'utf-8'))
        f.close()
    return export_result

def import_key(passphrase_txt, keyfile):
    key_data = open(keyfile, 'rb').read()
    import_result = gpg.import_keys(key_data, passphrase=passphrase_txt)
    return import_result.fingerprints

def list_public_keys(keyname):
    if keyname:
        return gpg.list_keys(keys=keyname)
    return gpg.list_keys()

def delete_public_key(keyname, passphrase):
    for fps in list_public_keys(keyname):
        gpg.delete_keys(fps['fingerprint'], passphrase=passphrase,  expect_passphrase = False)
    return True

def list_private_keys():
    return gpg.list_keys(True)

def encrypt_file(recipient, file_in):
    with open(file_in, 'rb') as f:
        status = gpg.encrypt_file(
            f, recipients=[recipient],
            output=file_in+'.gpg'
        )
    return status

def encrypt_and_sign_file(recipient, passphrase, file_in):
    with open(file_in, 'rb') as f:
        status = gpg.encrypt_file(
            f, recipients=[recipient],
            sign=True,
            passphrase=passphrase,
            output=file_in+'.gpg'
        )
    return status

def decrypt_file(passphrase, file_in):
    with open(file_in+'.gpg', 'rb') as f:
        status = gpg.decrypt_file(f, passphrase=passphrase, output=file_in)
    return status

def verify_and_decrypt_file(passphrase, file_in):
    with open(file_in+'.gpg', 'rb') as f:
        status = gpg.decrypt_file(f, passphrase=passphrase, output=file_in)
    return status

def encrypt_txt(input_txt, recipient):
    encrypted_data = gpg.encrypt(input_txt, recipient)
    return str(encrypted_data)

def decrypt_txt(input_data, passphrase):
    decrypted_data = gpg.decrypt(input_data, passphrase=passphrase)
    return decrypted_data

def main():
    NAME = 'Marv Drake'
    NAME_EMAIL = 'blah11@blah.com'
    NAME_COMMENT = 'this 12 a longish comment'
    PASS_PHRASE = 'imaG00Done'
    initialize(NAME, NAME_EMAIL, PASS_PHRASE, NAME_COMMENT)

main()