#ingreso de datos  parte del usario
nombre = input('¿como te llamas? ')# imprimimos una cadena y el dato ingresado por nosotros quedara asignado como valor de la variable nombre la cual siempre sera una cadena de texto.
print('Hola ' + nombre) # imprimira la cadena  la valor de la variable ingresada por el usuario

edad = input('¿Cuantos añor tienes? ')
print(type(edad))
print(f'{nombre} tiene {edad} años')

numero1= int(input('Introduce un numero por favor ')) #de esta manera en un 'int' solo paso conviertes la cadena ingresara por el ususario a una variable entero con la que si se puedesn hacer operaciones aritmeticas
numero2 = int(input('Introduce un numero por favor '))
nuemro3 = numero1 + numero2

print(f'El resultado de la suma es {nuemro3}')