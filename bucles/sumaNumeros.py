#Pide un número N  y calcula la suma de todos los números desde 1 hasta N


try :
    #Pedir la variable N
    n = int(input('Ingrese un número : '))
    suma = 0

    #Ciclo

    for i in range(1,n+1) :
        suma+= i
    
    #Imprimir la suma
    print(f'La suma de 1 a N es {n} = {suma}')

except ValueError as error :
    print(f'Error : {error}')
finally :
    print("Fin del Ejercicio")