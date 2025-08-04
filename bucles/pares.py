# Muestra todos los números pares desde 2 hasta un número N introducido por el usuario.

try :

    #Pedir la variable N
    n = int(input("Ingrese un número : "))

    print(f'Pares desde 2 hasta {n} : ')

    #Ciclo
    for i in range(2, n  + 1) : 
        if i % 2 == 0 :
            print(i)


except ValueError as error :
    print(f'Error : {error}')
except Exception as error :
    print(f'Error inesperado : {error}')
finally :
    print("Fin del Ejercicio")