from cryptography.fernet import Fernet

#key = Fernet.generate_key()

file = open('key.key', 'rb')
#file.write(key)
key = file.read()
file.close()

print(key)

