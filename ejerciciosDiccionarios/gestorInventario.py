#Gestor de Inventario

#Crear la estructura de Datos
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


print("Creado Inventario")

try :
    #Tarea - Encontrar el stock total de un producto en todas las sucursales
    while True :
        print("\nMenú")
        print("1. Encontrar el stock total de un producto en todas las sucursales")
        print("2. Salir")

        opcion = int(input("\nIngrese su opción: "))

        if opcion == 2 :
            break
        elif opcion == 1 :
            producto = input("Ingrese el SKU del producto: ").upper()
            if producto in inventario :
                for sucursal,stock in inventario[producto]["sucursales"] :
                    print(f"{sucursal} - {stock}")
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
