from cryptography.fernet import Fernet

# Get the key from the file
file = open('key.key', 'rb')# The key will be the byte types
key = file.read()
file.close()

# Encode the message
message = input('Enter with the message: ')
encoded = message.encode()

encrypt = b""
decrypt = b""

while True:
    print('''
    [ 1 ] encrypt
    [ 2 ] decrypt
    [ 3 ] exit
    ''')
    user = int(input('What do you want do? '))
    if user == 1:
        # Encrypt the message
        f = Fernet(key)
        encrypted = f.encrypt(encoded)
        print(encrypted)
    elif user == 2:
        # Decrypt the message
        f2 = Fernet(key)
        decrypted = f2.decrypt(encrypted)
        #print(decrypted)
        # Decode the message
        original_message = decrypted.decode()
        print(original_message)
    elif user == 3:
        break
    else:
        print("Choose error!")

