#Reto: Pide al usuario una palabra. Luego, usando un bucle for, 
# recorre cada letra de la palabra. Imprime únicamente las letras que no son vocales.

#Pista: Dentro del bucle, usa una condición if para comprobar si la letra actual 
# no es 'a', 'e', 'i', 'o', 'u'.

from typing import Counter


try :
    #Pedir la variable palabra
    palabra = input("Ingrese una palabra : ")
    Counter = 'Palabras: '

    #Ciclo
    for i in range(len(palabra)) :
        #condicional
        if palabra[i] != 'a' and palabra[i] != 'e' and palabra[i] != 'i' and palabra[i] != 'o' and palabra[i] != 'u' :
           Counter += ' ' + palabra[i] 
    print(Counter)

except Exception as error :
    print(f'Error : {error}')

finally :
    print("Fin del Ejercicio") 