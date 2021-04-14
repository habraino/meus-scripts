#! usr/bin/python3.8

# Caesar Chiper

MAX_KEY_SIZE = 26

def getMode():
    while True:
        print('Do you wish to encrypt or decrypt or brute force a message?')
        mode = input().lower()

        if mode in 'encrypt e decrypt d brute b'.split():
            return mode[0]
        else:
            print('Enter either "encript" or "e" or "decrypt" or "d" or "brute" or "b".')

def getMessage():
    print('Enter your message: ')
    return input()

def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%d)'%(MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= MAX_KEY_SIZE
                elif num < ord('A'):
                    num += MAX_KEY_SIZE
            elif symbol.islower():
                if num > ord('z'):
                    num -= MAX_KEY_SIZE
                elif num < ord('a'):
                    num += MAX_KEY_SIZE
            translated += chr(num)
        else:
            translated += symbol
    return translated

mode = getMode()
message = getMessage()

if mode[0] != 'b':
    key = getKey()

print('Your translated text is: ')
if mode[0] != 'b':
    print("\033[1;36m%s\033[m"%getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print("\033[1;34m[%d] \033[m\033[1;36m%s\033[m"%(key, getTranslatedMessage(mode, message, key)))
