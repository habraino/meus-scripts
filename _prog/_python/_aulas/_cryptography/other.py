import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

txt = input('Enter with text to encrypt: ')

password_provide = txt # This is input in the form of string
password = password_provide.encode()# Convert to type bytes

salt = b'\xcc\x17\x9d\x1b\x97\xc8\xf7\x81\x13\xf1\n\x91\xb82^\t'
kdf = PBKDF2HMAC(
    algorithm = hashes.SHA256,
    length = 32,
    salt = salt,
    iterations = 100000,
    backend = default_backend()
)

key = base64.urlsafe_b64encode(kdf.derive(password))# Can only use kdf once
print(key)
