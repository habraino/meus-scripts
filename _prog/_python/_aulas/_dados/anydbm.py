import anydbm

db = anydbm.open('db.dat', 'c')
db['she'] = 'ela'
db['he'] = 'ele'

for k, v in db.iteritems():
    print(k, '\t', v)

db.close()
