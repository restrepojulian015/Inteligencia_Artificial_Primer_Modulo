#Muestra un menú con 3 opciones (1. Ver saldo, 2. Depositar, 3. Retirar). 
# Pide al usuario que elija una y muestra un mensaje confirmando la elección.

print("=======Menú=======")
print("1. Ver saldo")
print("2. Depositar")
print("3. Retirar")
print("==================")

try: 
    #Pedir la variable opcion
    opcion = int(input("Ingrese su opción: "))

    #Condicional
    if opcion == 1 :
        print("Ver Saldo")
    elif opcion == 2 :
        print("Depositar")
    elif opcion == 3 :
        print("Retirar")
    else :
        print("Opción no valida")
except Exception as error:
    print(f'Error: {error}')
finally:
    print("Fin del Ejercicio")