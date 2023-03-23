def agragar_datos(lista, valor):
    '''Funcion que agrega una dato a un alista especifica'''
    if valor == '':
        valor = 'No especificado'
    lista.append(valor)
    return lista




nombres = []
edades = []
sexos = []

personas =int(input('¿Cuantas personas se desea registrar? '))

for i in range(personas):
    nombre = input(f'Ingrese el nombre de la persona {i +1}:').title()
    nombres = agragar_datos(nombres, nombre)
for i in range(personas):
    edad = input(f'Ingrese la edad de {nombres[i]}')
    edades = agragar_datos(edades, edad)
for i in range(personas):
    sexo = input(f'Cual es el sexo de {nombres[i]}')  
    sexos = agragar_datos(sexos, sexo)

for i in zip(nombres, edades, sexos):
    print(i)

