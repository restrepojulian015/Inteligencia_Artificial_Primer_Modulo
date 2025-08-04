#El programa elige un número secreto. El usuario tiene que adivinarlo. 
# El bucle continúa hasta que el usuario acierte.

try :
    
    numeroSecreto = 7

    #Bucle while
    while True :
        numero = int(input("Adivinar el número secreto:"))

        if numero == numeroSecreto :
            print("Correcto!")
            break
        else :
            print("Incorrecto")

except ValueError as error :
    print(f'Error : {error}')
except Exception as error :
    print(f'Error inesperado : {error}')
finally :
    print('Fin de la ejecución')