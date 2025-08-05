#Agrega un elemento al final de la lista.
#Este es uno de los métodos más comunes. Simplemente añade el elemento que le pases como argumento al final de la lista existente.

try :
    
    #Definir la lista
    lista = []
    
    while True:
        #Pedir al usuario un elemento
        elemento = input("Ingrese un elemento a la lista : ").lower()
        
        if elemento == "salir":
            break
        else:
            #Agregar el elemento a la lista
            lista.append(elemento)
            print(f'Lista actual : {lista}')
    
except Exception as error :
    print(f'Error : {error}')
finally :
    print("Fin del ejercicio")