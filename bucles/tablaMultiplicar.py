#Pide un número al usuario y muestra su tabla de multiplicar del 1 al 10

try : 
    #Pedir la variable número
    numero = int(input("Ingrese un número : "))

    #Ciclo
    for i in range(1,11) :
        resultado = numero * i
        print(f'{numero} x {i} = {resultado}')
except ValueError as error :
    print(f'Error : {error}')
finally :
    print("Fin del ciclo")