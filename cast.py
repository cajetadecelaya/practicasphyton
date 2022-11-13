# cast nos sirve para comvertir una cadena en un numero con el qu ese puedan hacer operaciones.
numero = '147'
print(numero)
print(type(numero))

numero = int (numero) # con esta variable extraes la cadena numero y la combierte en un entero
print(numero)
print(type(numero))

numero = float(numero) # con esta variable extraes la cadena numero y la combierte en un flotante
print(numero)
print(type(numero))

numero = complex(numero) # con esta variable extraes la cadena numero y la combierte en un complejo
print(numero)
print(type(numero))

bandera = 0
print(bandera)# a este punto se implime bandera como numero entero
print(type(bandera)) # a este punto se implime el tipo de variable como int
bandera = bool(bandera) # se convierte entero en false
print(bandera)
print(type(bandera))

help('keywords') # aqui nos mostrara la lista de palabras reservadas en python


