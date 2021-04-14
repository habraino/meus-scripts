from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.model_selection import train_test_split 
import numpy as np

iris = load_iris()

data = iris.data
target = iris.target 

modelo = KNN(n_neighbors=1)

X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=0)

# efetua o trinamento do modelo
modelo.fit(X_train, y_train)

novo = np.array([[5, 2.9, 1, 0.22]])

predict = modelo.predict(novo)

print(f"Classe: {predict}")
print(f"Pertence a especie: {iris['target_names'][predict]}")


