p_count = dict()

name_file = input("Enter with name of file: ")

file = open(name_file, 'r')

for line in file:
    words = line.split()
    for word in words:
        p_count[word] = p_count.get(word, 0) + 1
        
words = p_count.keys()

for word in words:
    print("Word: '{}' Quantity: {}".format(word, p_count[word]))
file.close()
