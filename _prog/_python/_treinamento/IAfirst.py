from sklearn import tree

lisa = 1
ireg = 0
maca = 1
laranja = 0

pomar = [[150, lisa], [130, lisa], [180, ireg], [160, ireg]]
res = [maca, maca, laranja, laranja]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(pomar, res)

peso = input("Entre com o peso: ")
sup = input("Entre com a superficie[0=irregular, 1=lisa]: ")

resUser = clf.predict([[peso, sup]])

if resUser == 1:
    print("É uma maça")
else:
    print("É uma laranja")

