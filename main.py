import pandas as pd
import numpy as np

# Cargar archivo CSV
df = pd.read_csv('Datos.csv')

# Mostrar información inicial sobre el dataframe
df.info()

# # Verificar si hay valores nulos
print("LLLLL")
df.isnull().sum()

# Limpiar datos eliminando o reemplazando valores nulos
df.fillna(value={'columna_con_nulos': 'valor_reemplazo'}, inplace=True)
# O eliminar filas si es necesario
df.dropna(inplace=True)
