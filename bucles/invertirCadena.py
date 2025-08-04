#Pide una palabra y muéstrala al revés.

try :

    #Pedir Cadena
    cadena = input("Ingrese una palabra : ")
    
    #Ciclo
    for i in range(len(cadena), -1, -1) :
        print(cadena[i-1])
except Exception as error :
    print(f'Error : {error}')
finally :
    print('Fin de la operación')