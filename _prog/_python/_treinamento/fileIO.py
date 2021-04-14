with open('foo.txt', 'w') as file:
    s = "My name is Hebraino de Deus"
    print(s)
    print(s, file=file)

    myfile = None
    print(s, file=myfile)
    print(s, file=None)


