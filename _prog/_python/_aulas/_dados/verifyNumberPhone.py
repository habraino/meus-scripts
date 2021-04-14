def verify(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for j in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for k in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office. And 999-263-5467 is my house.'
for i in range(len(message)):
    chunck = message[i:i+12]
    if verify(chunck):
        print("Phone number found: "+chunck)
print('Done')        

