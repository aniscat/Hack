import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt
import seaborn as sns

#Modelo de Regresion Lineal para aproximar las calificaciones segun  el genero, nivel educativo de los padre
 #Si se preparo para los examenes

dataset = pd.read_csv('Estudiantes.csv')  # Reemplaza 'tu_archivo.csv' con el nombre de tu archivo CSV

X = dataset[['Genero', 'Etnia', 'Nivel educativo de los padres', 'Examen de preparacion']]
y = dataset[['Matematicas', 'Lectura', 'Escritura']]  # Consideramos las tres calificaciones como variable objetivo

X = pd.get_dummies(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Evaluando modelo
train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)

train_rmse = mean_squared_error(y_train, train_predictions, squared=False)
test_rmse = mean_squared_error(y_test, test_predictions, squared=False)

print("RMSE en el conjunto de entrenamiento:", train_rmse)
print("RMSE en el conjunto de prueba:", test_rmse)

# Hacer una prediccion 
new_student = pd.DataFrame({'Genero': ['Femenino'], 'Etnia': ['Grupo B'], 
                            'Nivel educativo de los padres': ['Licenciatura, Ingenieria'], 
                            'Examen de preparacion': ['No realizado']})

new_student_encoded = pd.get_dummies(new_student, columns=['Genero', 'Etnia', 'Nivel educativo de los padres', 'Examen de preparacion'])

missing_cols = set(X.columns) - set(new_student_encoded.columns)
for col in missing_cols:
    new_student_encoded[col] = 0

new_student_encoded = new_student_encoded[X.columns]

# Crear prediccion
prediction = model.predict(new_student_encoded)
print("Prediccion de Calificaciones para el Nuevo Estudiante:")
print(prediction)

print("\nExploracion de Variables:")
print(dataset.describe())

poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X_train)
model_poly = LinearRegression()
model_poly.fit(X_poly, y_train)

train_predictions_poly = model_poly.predict(X_poly)
train_rmse_poly = mean_squared_error(y_train, train_predictions_poly, squared=False)
print("\nRMSE con Variables Polinomiales en el conjunto de entrenamiento:", train_rmse_poly)

from sklearn.linear_model import RidgeCV
model_ridge = RidgeCV(alphas=[0.1, 1.0, 10.0])
model_ridge.fit(X_train, y_train)

train_predictions_ridge = model_ridge.predict(X_train)
test_predictions_ridge = model_ridge.predict(X_test)

train_rmse_ridge = mean_squared_error(y_train, train_predictions_ridge, squared=False)
test_rmse_ridge = mean_squared_error(y_test, test_predictions_ridge, squared=False)

print("\nRMSE con Regularizacion en el conjunto de entrenamiento:", train_rmse_ridge)
print("RMSE con Regularizacion en el conjunto de prueba:", test_rmse_ridge)

# Grafica
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(train_predictions, train_predictions - y_train, c='blue', marker='o', label='Datos de Entrenamiento')
plt.scatter(test_predictions, test_predictions - y_test, c='orange', marker='*', label='Datos de Prueba')
plt.xlabel('Predicciones')
plt.ylabel('Residuos')
plt.title('Gráfico de Residuos')
plt.legend()

numeric_columns = dataset.select_dtypes(include=['int64', 'float64']).columns
numeric_data = dataset[numeric_columns]
correlation_matrix = numeric_data.corr()
plt.subplot(1, 2, 2)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Matriz de Correlacion')

plt.tight_layout()
plt.show()
