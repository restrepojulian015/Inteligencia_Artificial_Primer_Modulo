#Pide una contraseña. si tiene menos de 8 caracteres, di que es "demasiado corta". Si tiene 8 o más, di que es "valida".

try:
    #pedir contraseña
    contrasenia = input('Ingresa tu contraseña : ')

    #Condicional
    if len(contrasenia) < 8 :
        print('Demasiado corta')
    else :
        print('Valida')
except Exception as error:
    print(f'Error: {error}')
finally :
    print('Fin del Ejercicio')