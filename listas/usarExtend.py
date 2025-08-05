#Usar extend()

try :
    
    #Iniciar la primera lista
    lista1 = []
    
    #Iniciar la segunda lista
    lista2 = []
    
    #Bucle para agregar
    while True:
        #Pedir al usuario elepción
        eleccion = int(input("Ingrese 1 para agregar a la primera lista o 2 para la segunda lista o 0 para Salir: "))
        
        if eleccion == 0:
            break
        elif eleccion == 1:
            
            #Pedir al usuario un elemento
            elemento = input("Ingrese  un elemento a la lista 1:").lower()
            lista1.append(elemento)
            print(f'Lista 1 actual : {lista1}\n')
        elif eleccion == 2:
            
            #Pedir al usuario un elemento
            elemento = input("Ingrese un elemento a la lista 2: ").lower()
            lista2.append(elemento)
            print(f'Lista 2 actual : {lista2}\n')
    
    #Variable para elegir usar el .extend()
    usar_extend = input('¿Desea fucionar las dos listas? (SI/NO) : ').upper()
    
    if usar_extend == 'SI' :
        if len(lista1) < 0 or len(lista2) < 0 :
            
            print('No se puede fucionar las listas porque una de ellas está vacía')
        else :
            #Fucionar las listas
            lista3 = lista1.copy()
            lista3.extend(lista2)
            print(f'Fución de las listas : {lista3}')

except ValueError as error :
    print(f'Error de Valor : {error}')
except Exception as error :
    print(f'Error de Tipo : {error}')
finally :
    print("Fin del ejercicio")