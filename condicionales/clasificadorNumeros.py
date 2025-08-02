# Pide un número al usuario e indica si espositivo, negativo o cero


try:
    numero = int(input("Ingrese un número: "))

    if numero > 0 :
        print(f'El número {numero} es positivo')
    elif numero < 0 :
        print(f'El número {numero} es negativo')
    else :
        print(f'El número {numero} es cero')
except ValueError as error:
    print(f'Error: {error}')
finally :
    print('Fin de la operación')