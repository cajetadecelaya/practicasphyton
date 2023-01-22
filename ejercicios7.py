lista = []
alumnos = 0
while alumnos <=5 :
    opcion = input('Ingregar alumno (1) o terminar (2): ')
    if opcion == '1':
        nombre= input('Ingrese el nombre del alumno: ').capitalize()
        calificacion1 = int(input(f'Ingrese la primera calificacion de {nombre}: '))
        calificacion2 = int(input(f'Ingrese la segunda calificacion de {nombre}: '))
        alumno = [nombre, calificacion1, calificacion2]
        alumnos += 1
        lista.append(alumno)
    elif opcion == 2:
        print(f'El programa ha terminado con {alumnos} alumnos.')
        break
    else:
        print('Se ha ingresado una opcion no valida') 
        continue
       
print('La lista de alumpnos es: ')
print(lista)        