#Reto: Pide al usuario que introduzca 5 números, 
# uno por uno. Al final, dile cuántos de esos números eran pares.
#Pista: Necesitarás un bucle for que se repita 5 veces y un contador. 
# Dentro del bucle, usa if con el operador módulo (%) para verificar si el número es par.

try :

    contador = 0;

    #Ciclo
    for i in range(5) :
        #Pedir la variable número
        numero = int(input("Ingrese un número : "))

        #Condicional
        if numero % 2 == 0 :
            contador += 1

    print(f'El número de pares es : {contador}')

except ValueError as error :
    print(f'Error : {error}')
except Exception as error :
    print(f'Error inesperado : {error}')
finally :
    print("Fin del Ejercicio")