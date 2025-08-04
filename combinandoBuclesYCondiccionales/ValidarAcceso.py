#Reto: El programa debe seguir pidiendo un PIN de 4 dígitos hasta que el usuario introduzca "2025". Si el PIN introducido no tiene exactamente 4 dígitos, muestra un mensaje de error.
#Pista: Un bucle while es ideal. Dentro, usa un if con len() para verificar la longitud de la entrada. Si la longitud es correcta, comprueba si el PIN es "2025".

try :

    while True :

        #Pedir el pin a validar
        pin = int(input("Ingrese el pin: "))

        #condicional
        if len(str(pin)) != 4 :
            print("Error : El pin debe tener 4 digítos")
        elif pin == 2025 :
            print("Acceso Exitoso")
            break
        else :
            print("Acceso Denegado")
except ValueError as error :
    print(f'Error : {error}')
except Exception as error :
    print(f'Error : {error}')
finally :
    print("Fin del Ejercicio")