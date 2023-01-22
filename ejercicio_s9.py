#Utilizar al menos 2 funciones
#pregiuntar cuanto alumnos se registraran en caso de no ingresar un na cantidad se asume que se registraran 3 alumnos
#preguntar el nomte de 2 calificaciones
#Mostrar el nombte en pantalla con inicial mayusculas y promedio
#Al finalizar el programa se mostrara una lista con el nombre de cada alumno y sus calificaciones


def captura_alumnos(numero=3):
    """Funcion que registra alumos y dos calificaciones, recibe como parametro la cantidad de alumnos
    a registrar, si no se especifica el numero de alumnos , se registraran 3"""
    lista_alumnos = []  #se genera lista donde se guardaran los nombres de los alumnos
    for i in range(numero): #ciclo del numero de alumnos 
        nombre = input('Ingrese el nombre del alumno: ').capitalize()  #se ingresa el nombre  y se convierte a mayusculacon la funcion .capitalize
        calificacion1 = int(input(f'Ingrese la primera calificaccio de {nombre}:'))
        calificacion2 = int(input(f'Ingrese la segunda calificaccio de {nombre}:'))
        lista_alumnos.append([nombre,calificacion1, calificacion2])  # se ingresaran los datos ingresados a la lista
        promedio(nombre, calificacion1, calificacion2)
    print(lista_alumnos[])

def promedio(nombre, calificacion1, calificacion2):
    """calcula el promedio de un lalumno y lio desplilega en pantalla poor medio de un mensaje
    Recibe como parametro el nombre de dos calificaciones del alumno"""
    promedio = (calificacion1 +calificacion2) /2
    print(f'El promedio de {nombre} es: {promedio}')



numero_alumnos = input('Cuantos alumnos desea registrar? ')

if numero_alumnos.isdigit():
    numero_alumnos = int(numero_alumnos)
    captura_alumnos(numero_alumnos) #funcion 1, la cantidad de alimnos designados como 3 sera reasignado con la cantidad de alumnos que ingrese el usuario
else:
    captura_alumnos()    