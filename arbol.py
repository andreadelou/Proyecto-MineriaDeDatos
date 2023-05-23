import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Cargar los datos desde un archivo CSV
df = pd.read_csv('archivo_filtrado.csv')

# Dividir los datos en características y la etiqueta objetivo
X = df.drop('CLAUNI', axis=1)
y = df['CLAUNI']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Crear el modelo de árbol de decisión
clf = DecisionTreeClassifier(
    criterion='gini', max_depth=None, min_samples_leaf=1)

# Entrenar el modelo
clf.fit(X_train, y_train)

# Hacer predicciones sobre el conjunto de prueba
y_pred = clf.predict(X_test)

# Evaluar el rendimiento del modelo
print("Accuracy:", accuracy_score(y_test, y_pred))
