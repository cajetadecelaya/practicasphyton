#Ejemplo de la funcion print

# print('Hola Mundo')
# print('Hola mundo', 'otra vez')
# print('son las', 9, 'de la mañana')
# print('El resultado de 3 * 4 es:' , 3*4)

# Ejemplo de cadenas formatiadas
# print('El numero 15  en sistema decimal el %d, en sistema octal es %o, en el sistema hexadecimal es %x' %(15, 15, 15))

# pi = 3.141592
# r = 5
# print(f'El radio de un circulo es {r} y el area de ese circulo es {pi * r **2 : .2f}')# .2f indica que el resultado solo arojara los primero dos decimales

# Impresion de caracteres especiales
print('La letra beta es: \n\t \u03B2')# imprima la letra beta con un salto de linea \(n), se hace una tabulacion colocando el resultado algunos espacios despues(\t) y se agrega el codificacion ascci (u0382).

#Caracteres de escape
print('Hola mundo', end = ' ')# aqui se define qu eentre una cada y otra no haya salto de linea si no qu ese impliaen la misma linea con solo un espacio enre ambas
print('otra vez', end = '\t')
print('y otra vez')# de esta manera la impresion de las 3 cadenas se arrojan sobre la misma linea.
