#Tienda Electronica

#Gestionaremos un inventario donde cada producto tiene un nombre, precio y stock en diferentes sucursales.
#Estructura de Datos:
#Un diccionario principal para el inventario, donde la clave es el SKU (ID del producto).
#El valor para cada SKU será otro diccionario con los detalles del producto (nombre, precio).
#Dentro de los detalles, una clave 'sucursales' contendrá una lista.
#Cada elemento de la lista será una tupla (nombre_sucursal, cantidad_en_stock).


from sys import excepthook
from time import process_time_ns


try : 

    #Estructura de Datos
    inventario = {
        "SKU001": {
            "nombre": "Teclado Mecánico RGB",
            "precio": 75.50,
            "sucursales": [
                ("Bogotá - Centro", 15),
                ("Medellín - Poblado", 10)
            ]
        },
        "SKU002": {
            "nombre": "Mouse Gamer Inalámbrico",
            "precio": 49.99,
            "sucursales": [
                ("Bogotá - Centro", 25),
                ("Cali - Sur", 12)
            ]
        },
        "SKU003": {
            "nombre": "Monitor Curvo 27 pulgadas",
            "precio": 320.00,
            "sucursales": [
                ("Medellín - Poblado", 5),
                ("Bogotá - Norte", 8)
            ]
        }
    }
    print("Inventario inicial creado.")

    #Tarea - Encontrar el stock total de un producto en todas las sucursales

    while True : 
        print("\n Menú")
        print("1. Encontrar  el stock total de un producto.")
        print("2. Listar todos los productos en la Sucursal Bogotá - Centro.")
        print("3. Salir")

        opcion = int(input("\nIngrese su opción: "))

        if opcion == 3 :
            break
        elif opcion == 1 :
            producto = input("Ingrese el SKU del producto: ").upper()
            if producto in inventario :
                for sucursal,stock in inventario[producto]["sucursales"] :
                    print(f"{sucursal} - {stock}")
            else : 
                print("Error : El producto no existe")
        elif opcion == 2 :
            producto = input("Ingrese el SKU del producto: ").upper()
            if producto in inventario :
                for sucursal,stock in inventario[producto]["sucursales"] :
                    if sucursal == "Bogotá - Centro" :
                        print(f"{sucursal} - {stock}")
                    else :
                        print("Error : El producto no existe")
            else :
                print("Error : El producto no existe")
        else :
            print("Error : Opción no valida")
except ValueError as error :
    print(f'Error : {error}')
except KeyError as error :
    print(f'Error : {error}')
except Exception as error :
    print(f'Error : {error}')
finally :
    print("Fin del Ejercicio")