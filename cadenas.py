texto_variado = 'Palabre 123 +-* #%&'
print(type(texto_variado))

podemos utiliar comillas triples para que el texto se muertre como la cadena que hemos escrito
print('''
# funcionamiento de \n  #\n nos permite generar un salto de linea entre la cadena que esta antes y despues de n
# programa: (opciones)
# -1 Para acceder acciones
# -2 para salir''')

subscripting e indexado

####################################################
 texto = 'Python'  
En este ejemplo podemos imprimir un indice o caracter de la cadena 'Python' acorde a la posicion del valor
0=P, 1=y, etc

print(texto[0]) 
print(texto[5])
print(texto[-1])
print(texto[-6])
print(texto[6])  #error! no podemos acceder  a una posicion que no existe
print(texto[-7]) #error! no podemos acceder  a una posicion que no existe

letra = texto[0]
print(letra)


letra = 'p'
print(letra)

texto_compuesto = letra + texto[1] # concatenacion es la suma en cadenas de textos
print(texto_compuesto)

#######################################################
slicing o substringing  
sisrve para seleccionar un rango de indices
texto = 'Python'

print(texto[0:3])  # aqui solo se ha impreso los primeros 3 caracteres = 'Pyt'
print(texto[0:-3]) #inicia imprecion desde el indice 0 al indice tercero negativo = 'Pyt'
print(texto[0:-2]) # inicia ompesion del indice 0 al 2 negativo = 'Pyth
print(texto[2:]) # desde el indice 2 hasta el final = 'Thon'
print(texto[:3]) #impirme del inicio de la cadena hacia los 3 primeros indices ='Pyt'
print(texto[:-2]) #'Pyth'
print(texto[2:-2]) #'th'
print(texto[4:-2]) #' '
print(texto[-3::-1]) #htyP
print(texto[::-1]) #nohtyP
print(texto[2::-1]) #typ
print(texto[1:50]) #aqui se pide qu ese imprima los indicendesde el 1 hasta el 50cuenta pero aun qu eno cuente la cadena con ciertos caracteres este no arrojara erros y solo imprimira loscaracteres exstentes.
print(texto[2:2]) 

########################################################3
Cadenas y formatos

texto = 'Hola mundo! Buenas tardes'
print(texto.lower()) #La cadena texto se une a un metodo o herramienta mediante un  punto y lower convierte todo el texto en minusculas
print(texto.upper())#La cadena texto se une a un metodo  o herramienta mediante un  punto y upper convierte todo el texto en mayusculas
print(texto.capitalize()) #La pimer letra solamente como mayuscula
print(texto.title()) #La primer letra de cada palabra sera mayuscula
print(texto.swapcase()) #Intercambia minusculas con mayusculas
 
###formateado
print('{} + {} = {}'.format(2, 3, 2+3)) # 2 + 3 = 5. aqui los valores seran asignado en el mismo orden en los que se muestran en el metodo format
print('{} + {} = {}'.format('Hola', 'mundo', 'Hola mundo')) #Hola + mundo = Hola mundo aqui los valores seran asignado en el mismo orden en los que se muestran en el metodo format
print('{:.3f} + {:.4f} = {}'.format(2,3,2+3)) # 2.000 + 3.0000 =5 (.3f y .4f) definen la cantidad de decimales que mostrara el valor asignado en format
print('{1} + {0} = {2}'.format(2, 3, 2+3)) # al agregar los numeros entre los corchetes definicmos que valor se le asignara segun la posicion del indice  de la cadena
print('{1} + {0} = {2}'.format('Hola', 'mundo', 'Hola mundo')) # al agregar los numeros entre los corchetes definicmos que valor se le asignara segun la posicion del indice  de la cadena = mundo + Hola = Hola mundo
print('{:d} ={:b} = {:o} = {:x}'.format(15, 15, 15, 15)) #15, 1111, 17, f  decimal, binairo, octal y hexadecimal mismo valor pero en diferentes sistemas numerircos







