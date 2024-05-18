import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv('Estudiantes.csv') 

print("\nEstadisticas descriptivas:")
print(dataset.describe())

numerical_columns = dataset.select_dtypes(include=[np.number]).columns
correlation_matrix = dataset[numerical_columns].corr()
print("\nMatriz de Correlacion:")
print(correlation_matrix)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Matriz de Correlacion')
plt.show()
