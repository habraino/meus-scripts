def histogram(s):
    d = dict()
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
        
    return d

if __name__ == '__main__':
    h = histogram('python is the better')
    print(h)
