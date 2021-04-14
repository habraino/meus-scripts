a = ["blue", "red", "black", "white"]
b = ["cyan", "gray", "yellow", "brown", "pink"]

_set1 = set(a)
_set2 = set(b)

# imprime os sets
print("set_1: %s"%(_set1))
print("set_2: %s"%(_set2))

# apresenta diferença entre sets
print("difference: %s"%(_set1.difference(_set2)))

# uni os sets
print("union: %s"%(_set1.union(_set2)))

# interseção entre os sets
print("intersection: %s" %(_set1.intersection(_set2)))

# verifica se têm algo em comum
print(_set1.isdisjoint(_set2))
