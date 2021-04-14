#!python3

#passwordRobuts.py -> Detecta se um password é robusto

import re

def getPassword(password):
    p = re.compile(r'\d+\w+\W+')

    if len(password) >= 8:
        l = p.search(password)
        if l != None:
            print('\033[1;36mGood Password.\033[m')
        else:
            print('\033[1;31mPassword no robust\033[m')
    else:
        print("\033[1;33mPassword is low.\033[m")

getPassword('estuda1')
getPassword('ProgRamador')
getPassword('Askiki12@30')

