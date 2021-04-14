def divisivel(x, y):
    if x % y == 0:
        return True
    else:
        return False

if divisivel(4, 2):
    print('Sim')
else:
    print('Não')