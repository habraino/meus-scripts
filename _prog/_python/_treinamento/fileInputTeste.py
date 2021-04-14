import fileinput as file

replace = {'nome1':'Brayen',
           'nome2':'Hebraino'}

for line in file.input('foo.txt', inplace=True):
    for search_for in replace:
        replace_with = replace[search_for]

    print(line, end='')

