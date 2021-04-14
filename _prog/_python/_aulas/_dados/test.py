from cryptography.fernet import Fernet

# Get a key in byte
key = Fernet.generate_key()

# my message free
msg = input('Enter with message: ')

f = Fernet(key) # pass the params for f

encode = msg.encode()#  transform the message in bytes type

encrypt = f.encrypt(encode)# encrypt my message

print('The message encrypted: {}'.format(encrypt))# read my message encrypted

decrypt = f.decrypt(encrypt)
decode = decrypt.decode()
print('The message decrypted: {}'.format(decode))# read my message decrypted




