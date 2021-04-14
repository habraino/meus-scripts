import os

def is_empty_file(fpath):
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

print(is_empty_file('foo.txt') == True)
