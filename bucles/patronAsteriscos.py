#Pide un número N y dibuja un triángulo de asteriscos de N filas.

try :

    #Pedir la variable N
    n = int(input("Ingrese un número : "))

    #ciclo
    for i in range(1, n + 1) :
        print("*" * i)

except ValueError as error :
    print(f'Error : {error}')
except Exception as error :
    print(f'Error inesperado : {error}')
finally :
    print('Fin de la operación')