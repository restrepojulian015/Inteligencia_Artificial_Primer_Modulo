#Uso de CSV con Pandas

#importar pandas
import pandas as pd

#Especificar la ruta del archivo CSV

ruta_archivo = r"C:\Users\Usuario\Documents\train_and_test2.csv"

#Usar pd.read_csv para leer el archivo CSV
pd_titanic = pd.read_csv(ruta_archivo)

#Imprimir el CSV
print("Imprimir el CSV:")
print(pd_titanic)