a = [1, 2, 3, 4]

try:
    print(a[3])
except IndexError:
    print('Index not exists!')
finally:
    print("End of the test!")

    