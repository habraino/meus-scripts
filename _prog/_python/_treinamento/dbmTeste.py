import dbm

db = dbm.open("teste", "c")
db['brayen.png'] = 'This is a piture of Brayen'

for key in db:
    print(key, db[key])




