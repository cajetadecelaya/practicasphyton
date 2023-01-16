#Conjuntos no tiene un orden establecido pero solo se puede almacenar el dato una sola vez
canasta = {'manzana', 'naranja', 'manzana', 'pera', 'naranja', 'platano'}
print(canasta)

print('manzana' in canasta) #imprime true or false si esta el dato manzana en el conjunto canasta

### eliminar datos repetidos
vocales= ['a','e','i','o','u','e', 'a']
vocales = list(set(vocales)) #primero se convienrte la lista a un conjunto y volverlo a convetir a lista ['i', 'e', 'u', 'a', 'o']

print(vocales)

vocales1 = {'a','e','i','o','u','a'}
vocales2 = {'e','i','o'}

print(vocales2.issubset(vocales1)) #con la funcion .issubset nos muerts si un conjunta es contenido de otro contenido

####
vocales3 = {'a','e','i','o'}
vocales4 = {'E','I','O'}

print(vocales3 - vocales4) #se pueden restar  solo los valores similares entre conjuntos.
print(vocales3 | vocales4) #se pueden unir conjuntos 
print(vocales3 & vocales2) #muestra la intercepcion(valores repetidos) entre ambos conjuntos.
print(vocales1 ^ vocales4) #muestra la diferencia simetrica, es decir los conjuntos que no se repiten entre ambos conjuntos
