####las tuplas son coleccion de informacion que no pueden ser modificadas
vocales= ('a','e','i','o','u')
print(vocales[4: ])


print(vocales.index('u'))  # muestra el valor del indice qu ele corresponde a la 'u'

####

lista_vocales = list(vocales) #se creo una lista a parti de la tupla, esta si se puede modificar
lista_vocales[2]= 'o' #se remplaza el valor de la posicion 2 con la letra 'o'
print(f'tupal{vocales},  lista{lista_vocales}')

#####

