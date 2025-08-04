#Pide un número y calcula su factorial (ej: el factorial de 5 es 5 * 4 * 3 * 2 * 1).

try :

    #Pedir la varaible N
    n = int(input("Ingrese un número : "))
    resultado = 1

    for i in range(1, n+1 ) :
        resultado *= i
    
    print(f'El factorial de {n} es {resultado}')

except ValueError as error : 
    print(f'Error : {error}')
except Exception as error :
    print(f'Error inesperado : {error}')
finally :
    print("Fin del ejercicio")
