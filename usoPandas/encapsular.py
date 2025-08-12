#Seleccionar Series de un DataFrame

#Primer paso: importar pandas
import pandas as pd

#Segundo paso: Seleccionar la ruta del archivo csv
df_ejercicio = pd.read_csv(r"C:\Users\Usuario\AppData\Local\Temp\1bdd895f-57dd-4d59-b8f0-8012f22362b9_archive.zip.2b9\train_and_test2.csv")

#Segundo paso: Seleccionar la serie
age_serie = df_ejercicio['Age']

#Tercer paso: Verificar la carga correcta de la serie
print("Serie 'Age' del DataFrame:")
print(age_serie.head())


