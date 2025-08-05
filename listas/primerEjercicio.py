#Crea una lista vacía llamada lista_compras.
#Añade los siguientes productos a la lista: "Leche", "Pan", "Huevos", "Manzanas".
#Imprime la lista para verificar los productos.
#Después de revisar, te das cuenta de que ya tienes "Pan". Elimina "Pan" de la lista.
#Imprime la lista final.


try :
    
    #Crear listas llamada lista_compras
    lista_compras = []
    lista_compras.append("Leche")
    lista_compras.append("Pan")
    lista_compras.append("Huevos")
    lista_compras.append("Manzanas")
    
    #Bucle para imprimir la lista de Compras
    for i in range(4):
        print(lista_compras[i])
    
    lista_compras.remove("Pan")
    
    #Imprimir la lista final
    print(f'Lista final de compras: {lista_compras}')
    
except Exception as error :
    print(f'Error : {error}')
except ValueError as error :
    print(f'Error de Valor : {error}')
finally :
    print("Fin del ejercicio")