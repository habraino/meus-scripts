# file_name: file_cipher.py

from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isabs, join


class Encryptor:

    def __init__(self, key):
        self.key = key 

    def pad(self, f):
        return f + b'\0' * (AES.block_size - len(f) % AES.block_size)
    
    def encrypt(self, message, key, key_size = 256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)
    
    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            plainttext = fo.read()
        encrypt = self.encrypt(plainttext, self.key)

        with open(file_name + '.enc', 'wb') as fo:
            fo.write(encrypt)
        os.remove(file_name)
    
    def decrypt(self, cipherText, key):
        iv = cipherText[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv) 
        plainttext = cipher.decrypt(cipherText[AES.block_size:])
        return plainttext.rstrip(b'\0')
    
    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            cipherText = fo.read()
        decrypt = self.decrypt(cipherText, self.key)

        with open(file_name[:-3], 'wb') as fo:
            fo.write(decrypt)
        os.remove(file_name)

    def getAllFiles(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dirs = []
        for dirName, subDirList, fileList in os.walk(dir_path):
            for fname in fileList:
                if(fname != 'file_cipher.py' and fname != 'data.txt.enc'):
                    dirs.append(dirName + '\\' + fname)
        return dirs
    
    def encryptAll(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.encrypt_file(file_name)
    
    def decryptAll(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.decrypt_file(file_name)

key = b'H4\x1e\xac$\x85\x85\xa8\xbe\xf2\xa3\xa8\xde\xd6a\xab'
enc = Encryptor(key)
clear = lambda:os.system('clear')

if os.path.isfile('data.txt.enc'):
    while True:
        password = str(input('Enter with password: '))
        enc.decrypt_file('data.txt.enc')
        p = ''
        with open('data.txt.enc') as f:
            p = f.readlines()
        if p[0] == password:
            enc.encrypt_file('data.txt.enc')
            break

    while True:
        clear()
        choice = int(input('''
            1 → to encrypt file
            2 → to decrypt file
            3 → to encrypt all file
            4 → to decrypt all file
            5 → to exit\nWhat you want to do? 
            '''))
        clear()

        if choice == 1:
            enc.encrypt(str(input('Enter name of file to encrypt: ')))
        elif choice == 2:
            enc.decrypt(str(input('Enter name of file to decrypt: ')))
        elif choice == 3:
            enc.encryptAll()
        elif choice == 4:
            enc.decryptAll()
        elif choice == 5:
            exit()
        else:
            print('Please select a valid option!')
else:
    while True:
        clear()
        password = str(input('Enter with password for to decrypt: '))
        repassword = str(input('Confirm password: '))
        if password == repassword:
            break
        else:
            print('Passwords Mismatched!')
    
    file = open('data.txt', 'w+')
    file.write(password)
    file.close()

    enc.encrypt_file('data.txt')
    print('Please restart the program to complet the setup!')



