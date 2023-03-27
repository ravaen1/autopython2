import pandas as pd

# Leer los archivos de Excel en DataFrames
tabla_a = pd.read_excel('tabla_a.xlsx', sheet_name="Hoja1")
tabla_b = pd.read_excel('tabla_b.xlsx', sheet_name="Hoja1")

# Realizar la operación de búsqueda y combinación
tabla_b = tabla_b.merge(tabla_a[['SUMINISTRO', 'NUMEROFICHA']], on='SUMINISTRO', how='left')

# Guardar el resultado en un nuevo archivo de Excel
tabla_b.to_excel('tabla_b.xlsx', index=False) 
