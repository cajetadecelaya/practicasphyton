#Uso de la sentencia continuo en un siclo for

# for numero in range(1, 11):
#     if numero % 2==1:
#         continue   #si se cumple esta condicion no hara nada y brincara a la siguiente iteracion
#     print(f'{numero} es un numero par')

# #uso sentencia continue en u ciclo while
# numero = 0
# while numero <11:
#     numero +=1   
#     if numero % 2 == 0:
#         continue
#     print(f'{numero} es inpar') 
# #######################
# numero = int(input('Ingrese un digito: '))
# limite_inferior = 0
# limite_superior = 10
# buscado = 5
# intento = 0

# while True:
#     intento +=1
#     if numero == buscado:
#         print(f'El numero {numero} fue encontrado  en {intento} intentos')
#         break
#     elif numero > buscado:
#         limite_superior = buscado
#         buscado = (buscado + limite_inferior) //2
#     else:
#         limite_inferior = buscado
#         buscado = (buscado + limite_superior) //2    
#########################
#uso de la funcion exit

# numero = int(input('Ingrese un digito: '))
# limite_inferior = 0
# limite_superior = 10
# buscado = 5
# intento = 0

# while True:
#     intento +=1
#     if numero == buscado:
#         print(f'El numero {numero} fue encontrado  en {intento} intentos')
#         exit()
#     elif numero > buscado:
#         limite_superior = buscado
#         buscado = (buscado + limite_inferior) //2
#     else:
#         limite_inferior = buscado
#         buscado = (buscado + limite_superior) //2  
####################
# intento = 0
# while True:
#     intento +=1
#     print(f'Intentos {intento}')
#     if intento == 20:
#         print(' Fin de programa')
#         exit()
        