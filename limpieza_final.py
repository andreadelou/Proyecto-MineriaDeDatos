import pandas as pd

# Cargar los datos
data = pd.read_csv('archivo_limpio.csv')

# Filtrar los datos y eliminar las filas con valores que se deben ignorar
filtered_data = data[(data['EDADHOM'] < 150) & (data['EDADMUJ'] < 150) & (
    data['GETHOM'] < 5) & (data['GETMUJ'] < 5) & (data['CLAUNI'] < 5)]

# Crear un nuevo archivo con los datos filtrados
filtered_data.to_csv('archivo_filtrado.csv', index=False)
