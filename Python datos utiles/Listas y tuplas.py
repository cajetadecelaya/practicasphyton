####Lista y tuplas
#eje 1
# asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua'] # la lista se crea encerrando en corchetes.
# asignaturas2 = ('Matemáticas', 'Física', 'Química', 'Historia', 'Lengua') #la tupla se crea encerrando en parentesis.
# print(asignaturas)
# asignaturas.append('programacion')

#### Imprimir 'Yo estudio en (cada una de las asignaturas en la lista')
# Yo estudio asignatura Matemáticas
# Yo estudio asignatura Física
# Yo estudio asignatura Química
# Yo estudio asignatura Historia
# Yo estudio asignatura Lengua

# asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
# for asignatura in asignaturas:
#     print(f'Yo estudio asignatura {asignatura}')

####
#  la calificacion de Matemáticas: 6
# Ingrese la calificacion de Física: 7
# Ingrese la calificacion de Química: 85
# Ingrese la calificacion de Historia: 8
# Ingrese la calificacion de Lengua: 9
# La calificacion de Matemáticas es de: 6.0
# La calificacion de Física es de: 7.0
# La calificacion de Química es de: 85.0
# La calificacion de Historia es de: 8.0
# La calificacion de Lengua es de: 9.0

 
asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
notas = []  #Esta lista queda vacia para que se agreguen elementos por el usuario
for asignatura in asignaturas: #el valor  de asignatura lo designa el numero de elementos de la lista asignaturas
    calificacion = float(input(f'Ingrese la calificacion de {asignatura}: ')) #se ingresa el valor de la lista vacia notas.
    notas.append(calificacion) #ingresa un valor al final de la lista notas

for i in range(len(asignaturas)): #(len(asignaturas)) la longitud de la lista indicara valor a i ayudandonos a imprimir los elementos de manera requerida.
    print(f'La calificacion de {asignaturas[i]} es de: {notas[i]}')   