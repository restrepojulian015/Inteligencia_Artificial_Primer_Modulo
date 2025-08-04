#Pide las longitudes de los 3 lados de un triángulo y determina si es 
# equilátero (todos los lados iguales), isósceles (dos lados iguales) o escaleno (ningún lado igual).

try:
    #Pedir la varible lado1
    lado1 = int(input("Ingrese el lado 1: "))

    #Pedir la varible lado2
    lado2 = int(input("Ingrese el lado 2: "))

    #Pedir la varible lado3
    lado3 = int(input("Ingrese el lado 3: "))

    #Condicional
    if lado1 == lado2 and lado2 == lado3 :
        print("Equilatero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3 :
        print("Isoceles")
    else :
        print("Escaleno")

except ValueError as error:
    print(f'Error: {error}')

except Exception as error:
    print(f'Error inesperado: {error}')
finally: 
    print("Fin del proceso")