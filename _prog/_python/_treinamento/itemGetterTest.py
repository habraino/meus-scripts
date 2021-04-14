from itertools import groupby
from operator import itemgetter

d = {'a': 1, 'b': 5, 'c': 1}

a = dict((i, dict(v)) for i, v in groupby(d.items(), itemgetter(1)))
print(a)
