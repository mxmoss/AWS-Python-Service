@echo off
if %1!==! goto Usage
if %2!==! goto Usage
rem if %3!==! goto Usage
echo Generating a key for %1
echo at email %2
echo .
echo     %%echo Generating a basic OpenPGP key > buildkey.txt
echo     Key-Type: DSA >> buildkey.txt
echo     Key-Length: 1024 >> buildkey.txt
echo     Subkey-Type: ELG-E >> buildkey.txt
echo     Subkey-Length: 1024 >> buildkey.txt
echo     Name-Real: %1 >> buildkey.txt
echo     Name-Email: %2 >> buildkey.txt
echo     Name-Comment: %3 >> buildkey.txt
echo     Expire-Date: 0 >> buildkey.txt
echo     Passphrase: easyone23 >> buildkey.txt
echo     %%commit >> buildkey.txt
echo     %%echo done >> buildkey.txt

@echo on
gpg --batch --gen-key buildkey.txt
gpg --armor --export %2 > public_key.asc
@echo off
echo Import the file public_key.asc to the license server

goto End

:Usage
echo .
echo Usage
echo .
echo %0 "Name" email "comment"
echo     where "comment" is optional
echo .

:End

