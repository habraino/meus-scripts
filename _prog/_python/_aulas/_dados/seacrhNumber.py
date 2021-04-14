import re

padrao = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phone = padrao.search('My phone number is 223-453-3678')
print('Phone number found: '+phone.group())

print(phone.group(2))

