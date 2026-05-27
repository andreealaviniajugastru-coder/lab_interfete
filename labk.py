import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris=load_iris()
x = iris.data
y = iris.target
# print(iris)

print(x.shape)
print("Nr exemple:", x.shape[0])
print(iris.feature_names)
print(iris.target_names)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
print(x_train[:3])
knm = KNeighborsClassifier(n_neighbors=3)
knm.fit(x_train,y_train)
y_pred = knm.predict(x_test)
print(accuracy_score(y_test,y_pred))
#print("Acuratete model:", accuracy)

import matplotlib.pyplot as plt

# Liste pentru stocarea rezultatelor
k_values = range(1, 16)
accuracies = []

# Antrenare și evaluare pentru fiecare k
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)

    y_pred = knn.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)

    accuracies.append(accuracy)

# Afișarea acurateților
for k, acc in zip(k_values, accuracies):
    print(f"k={k}, acuratete={acc:.4f}")

# Grafic
plt.plot(k_values, accuracies, marker='o')
plt.xlabel("Valoarea lui k")
plt.ylabel("Acuratete")
plt.title("Acuratetea KNN in functie de k")
plt.grid(True)
plt.show()

# Valoarea optimă a lui k
best_k = k_values[accuracies.index(max(accuracies))]
print("Cel mai bun k:", best_k)
print("Acuratete maxima:", max(accuracies))

from sklearn.metrics import confusion_matrix, classification_report

# Predicții finale
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)

y_pred = knn.predict(x_test)

# 6.1 Matricea de confuzie
cm = confusion_matrix(y_test, y_pred)

print("Matricea de confuzie:")
print(cm)

# 6.2 Raport de clasificare
print("\nRaport de clasificare:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.neighbors import KNeighborsClassifier

# Model KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)

# Predicții
y_pred = knn.predict(x_test)

# 6.1 Matricea de confuzie
cm = confusion_matrix(y_test, y_pred)

print("Matricea de confuzie:")
print(cm)

# 6.2 Raport de clasificare
print("\nRaport de clasificare:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

from sklearn.metrics import confusion_matrix, classification_report
from sklearn.neighbors import KNeighborsClassifier

# Model KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)


#ex7,a
import matplotlib.pyplot as plt

#  2 caracteristici:
# petal length (index 2)
# petal width (index 3)

plt.figure(figsize=(8,6))

scatter = plt.scatter(
    x[:, 2],  # lungime petală
    x[:, 3],  # lățime petală
    c=y,
)

plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("Distribuția florilor Iris")

plt.legend(
    handles=scatter.legend_elements()[0],
    labels=iris.target_names
)

plt.show()
#b
import numpy as np

# Floare nouă:
# sepal length, sepal width, petal length, petal width
floare_noua = np.array([[5.1, 3.5, 1.4, 0.2]])

#  scalare
floare_noua_scaled = scaler.transform(floare_noua)

# Predicție
predictie = knn.predict(floare_noua_scaled)

#  rezultat
print("Clasa prezisă:", iris.target_names[predictie[0]])