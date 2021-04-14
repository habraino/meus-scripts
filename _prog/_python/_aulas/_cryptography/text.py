from cryptography.fernet import Fernet

file = open('key.key', 'rb') # key will be in bytes type
key = file.read() # read the key by file
file.close()


with open('arq.txt.encrypted', 'rb') as append:
    data = append.read()

f = Fernet(key)
encrypted = f.decrypt(data)

with open('arq.txt.decrypted', 'wb') as f:
    f.write(encrypted)
