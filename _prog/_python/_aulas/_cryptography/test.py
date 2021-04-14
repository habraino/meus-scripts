print('*'*45)
print('\tWelcome to encryptor programm!')
print('*'*45)

from cryptography.fernet import Fernet
from time import sleep
import os


# get key of file
file = open('key2.key', 'rb')
key = file.read()
file.close()

# variables global
clear = lambda:os.system('clear')
user = 0

while True:
	print('''
		[ 1 ] encrypt
		[ 2 ] decrypt
		[ 3 ] exit
	''')
	user = int(input('what you wonna do? '))
	if user == 1:
		clear() # clean the window
		# Get the message for user
		msg = input('Enter with the message: ')
		encoded = bytes(msg, 'utf-8') # transform the message in byte type

		# Encrypt the message readed for user
		f = Fernet(key)
		encrypt = f.encrypt(encoded)
		print(encrypt)
	elif user == 2:
		clear() # clean the window
		# Get the message for user
		msg = input('Enter with the message: ')
		# Decrypt the message
		decrypt = f.decrypt(encrypt)
		decoded = decrypt.decode()
		print(decoded)
	elif user == 3:
		break
	else:
		print('Please choose one option valid!')

# Exiting
print('Exiting...')
sleep(2)
clear()


