#Pide al usuario que introduzca 5 números, uno por uno, y al final muestra 
# cuál fue el número más grande.

try :
    numeroMayor = 0

    #Ciclo
    for i in range(5) :
        numero = int(input("Ingrese un número : "))

        if numero > numeroMayor :
            numeroMayor = numero

    print(f'El número mayor es : {numeroMayor}')

except ValueError as error : 
    print(f'Error : {error}')
finally :
    print("Fin del Ejercicio")