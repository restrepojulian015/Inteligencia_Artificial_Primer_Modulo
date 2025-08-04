#Sigue pidiendo al usuario una contraseña hasta que introduzca "1234".

try :

    #Peidr al usuario la contraseña
    contrasenia =  input("Ingrese la contraseña (1234) :")

    #Condicional
    while contrasenia != '1234' :
        contrasenia = input("Ingrese la contraseña correcta (1234) :")
    
    print("Contraseña correcta")

except Exception as error :
    print(f'Error : {error}')
finally :
    print("Fin del ejercicio")