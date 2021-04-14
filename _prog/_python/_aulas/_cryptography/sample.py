from cryptography.fernet import Fernet

key = Fernet.generate_key()

cipher_suite = Fernet(key)

txt = input("Enter with text to encrypt: ")
cipher_text = cipher_suite.encrypt(bytes(txt,'utf-8'))

print(cipher_text)

original_text = cipher_suite.decrypt(cipher_text)

print(original_text)
