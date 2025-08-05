#Sistema de Gestión de Cursos y Estudiantes

#Imagina que necesitas gestionar la información de varios estudiantes, 
# incluyendo sus datos personales y los cursos que han tomado con sus respectivas calificaciones.
#Estructura de Datos:
#Una lista principal para contener a todos los estudiantes.
#Cada estudiante será un diccionario con sus datos (id, nombre).
#Dentro del diccionario del estudiante, una clave 'cursos' contendrá una lista de los cursos.
#Cada curso en esa lista será una tupla (nombre_del_curso, calificacion), ya que la 
# calificación de un curso específico no debería cambiar una vez asignada.

#ESTRUCTURA DE DATOS
sistema_estudiantes = [
    {
        "id": 101,
        "nombre": "Ana García",
        "cursos": [
            ("Matemáticas", 95),
            ("Historia", 88),
            ("Programación", 100)
        ]
    },
    {
        "id": 102,
        "nombre": "Luis Martínez",
        "cursos": [
            ("Matemáticas", 82),
            ("Física", 91)
        ]
    },
    {
        "id": 103,
        "nombre": "Sofía Rodriguez",
        "cursos": [
            ("Programación", 89),
            ("Literatura", 92),
            ("Física", 95)
        ]
    }
]

print("Estructura de Datos inicializada")

try :

    promedio = 0

    #Calcular el promedio de un estudiante específico
    id_estudiante = int(input("Ingresa el ID del estudiante: "))

    for estudiante in sistema_estudiantes :
        if estudiante["id"] == id_estudiante :
            estudiante_objetivo = estudiante
            break
    if estudiante_objetivo :
        for i in estudiante_objetivo["cursos"] :
            promedio += i[1]
        promedio/= len(estudiante_objetivo["cursos"])
        print(f'El promedio del estudiante {id_estudiante} es : {promedio}')
    else :
        print(f'Error : No se encontro el estudiante con el ID {id_estudiante}')

except ValueError as error :
    print(f'Error : {error}')
except KeyError as error :
    print(f'Error : {error}')
except Exception as error :
    print(f'Error : {error}')
finally :
    print("Fin del Ejercicio")