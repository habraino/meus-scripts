def inverte(d):
    inv = dict()
    for k in d:
        v = d[k]
        if v not in inv:
            inv[v] = [k]
        else:
            inv[v].append(k)
    return inv

if __name__ == '__main__':
    d = {'nome':'Brayen', 'idade':21, 'morada':'Neves'}
    print(inverte(d))
