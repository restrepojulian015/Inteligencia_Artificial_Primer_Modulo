# Pregunta la edad y el país. Indica si puede votar (mayor de 18 en Colombia, mayor de 16 en Argentina).

try:
    #Pido la edad
    edad = int(input("Ingrese su edad: "))

    #Pido el país
    pais = input("Ingrese su país: ").upper()

    #Condicional
    if pais == "COLOMBIA" and edad >= 18 :
        print("Puedes votar")
    elif pais =="ARGENTINA" and edad >= 16 :
        print("Puedes votar")
    else :
        print("No puedes votar")
except ValueError :
    print(f'Error: {error}')
except Exception as error:
    print(f'Error inesperado: {error}')
finally:
    print('Fin de la operación')