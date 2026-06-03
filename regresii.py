from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

model = LinearRegression()
model.fit(x, y)

predictie = model.predict([[5]])
print(predictie)

from sklearn.datasets import load_diabetes


diabetes = load_diabetes()


print(diabetes)

#ex2
from sklearn.datasets import load_diabetes
import pandas as pd


diabetes = load_diabetes()

df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)

# afișarea primelor 5 rânduri
print(df.head())
#ex 3
from sklearn.datasets import load_diabetes

# încărcarea datasetului
diabetes = load_diabetes()

# afișarea
print(diabetes.feature_names)

# ex 4
from sklearn.datasets import load_diabetes
import pandas as pd


diabetes = load_diabetes()

df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)


print(df.describe())
# ex 5
from sklearn.datasets import load_diabetes
import pandas as pd
import matplotlib.pyplot as plt

# încărcarea datasetului
diabetes = load_diabetes()

# creare DataFrame
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)

# histogramă pentru BMI
plt.hist(df['bmi'])

# titlu și etichete
plt.title('Histograma BMI')
plt.xlabel('BMI')
plt.ylabel('Frecvență')

# afișare grafic
plt.show()
# ex 6
from sklearn.datasets import load_diabetes
import pandas as pd
import matplotlib.pyplot as plt

diabetes = load_diabetes()

df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)

#variabila
df['target'] = diabetes.target

# scatter plot: BMI vs target
plt.scatter(df['bmi'], df['target'])
plt.title('BMI în funcție de target')
plt.xlabel('BMI')
plt.ylabel('Target')
plt.show()

# scatter plot: Age vs target
plt.scatter(df['age'], df['target'])
plt.title('Age în funcție de target')
plt.xlabel('Age')
plt.ylabel('Target')
plt.show()

print("Exercițiul 7 - Regresie liniară simplă utilizând BMI")

# 7.a Alegerea variabilei de intrare și a țintei
X_bmi = df[["bmi"]]
y_target = df["target"]

# 7.b Împărțirea datelor în train și test
from sklearn.model_selection import train_test_split
X_train_bmi, X_test_bmi, y_train_bmi, y_test_bmi = train_test_split(X_bmi, y_target, test_size=0.2, random_state=42)

# 7.c Construirea și antrenarea modelului
model_bmi = LinearRegression()
model_bmi.fit(X_train_bmi, y_train_bmi)

# 7.d Predicții și reprezentare grafică
predictii_bmi = model_bmi.predict(X_test_bmi)

plt.figure(figsize=(8, 6))
plt.scatter(
    X_test_bmi,
    y_test_bmi,
    alpha=0.7,
    label="Valori reale"
)
plt.plot(
    X_test_bmi,
    predictii_bmi,
    linewidth=2,
    label="Dreapta de regresie"
)
plt.title("Legătura dintre BMI și scorul diabetului")
plt.xlabel("BMI")
plt.ylabel("Scor diabet")
plt.legend()
plt.show()

# 7.e Calculul erorii MSE
from sklearn.metrics import mean_squared_error, r2_score
eroare_mse = mean_squared_error(y_test_bmi, predictii_bmi)
print("MSE =", eroare_mse)

print("\nExercițiul 8 - Regresie liniară cu BMI și BP")

# 8.a Selectarea celor două caracteristici
X_multi = df[["bmi", "bp"]]
y_multi = df["target"]

# Împărțirea datelor
X_train_multi, X_test_multi, y_train_multi, y_test_multi = train_test_split(
    X_multi, y_multi, test_size=0.2, random_state=42
)

# 8.b Antrenarea noului model
model_multi = LinearRegression()
model_multi.fit(X_train_multi, y_train_multi)

# 8.c Afișarea coeficienților
print("Coeficient BMI:", model_multi.coef_[0])
print("Coeficient BP :", model_multi.coef_[1])

# 8.d Evaluarea modelului prin scorul R²
predictii_multi = model_multi.predict(X_test_multi)
scor_r2 = r2_score(y_test_multi, predictii_multi)

print("R² =", scor_r2)

