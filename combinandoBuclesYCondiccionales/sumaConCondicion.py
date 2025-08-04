#Reto: Pide al usuario un número N. Calcula la suma de todos los números del 1 al N, pero solo incluye en la suma aquellos que sean mayores a 5.
#Pista: Usa un bucle for y un acumulador. Dentro del bucle, un if debe comprobar si el número actual es mayor que 5 antes de sumarlo al total.

try :

    #Pedir la variable N
    n = int(input("Ingrese un número : "))
    suma = 0

    #Condicional
    if n < 5 :
        print("El número debe ser mayor a 5")
    elif n > 5 :
        for i in range(5, n+1) :
            suma += i
        print(f'La suma de 5 a {n} es {suma}')
except ValueError as error : 
    print(f'Error : {error}')
except Exception as error :
    print(f'Error inesperado : {error}')
finally :
    print("Fin del Ejercicio")