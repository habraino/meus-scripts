import json

d = {
    'nome': 'Brayen',
    'idade': 21,
    'morada': 'Neves'
}


# ------ Trabalhando com arquivos --------
with open('foo.txt', 'w') as f:
    json.dump(d, f)


with open('foo.txt', 'r') as r:
    d = json.load(r)
    for k, v in d.items():
        print(k, ' = ', v)

# Trabalhando com arquivo json
json_file_path = './data.json'
data = {'Languages': [{'name': 'Python', 'create_by': 'Guido Van Hossun', 'create_in': 1989},
                     {'name': 'Java', 'create_by': 'James Gosling', 'create_in': 1984}]}

with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=2)

d = json.dumps(data, indent=2, sort_keys=False, separators=(':', ' → '))
print(d)

