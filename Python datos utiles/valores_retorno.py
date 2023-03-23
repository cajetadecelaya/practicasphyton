# #valores de retorno, sentencia return

# def area(**dato): # dato es una variable que recibe un diccionario
#     """Calcula es alrea de una fgura geometrica y la impprime en pantalla"""
#     #si el diccionario tiene una clave llamada 'figura' evalua el valir de la clave
#     if dato['figura'] == 'Rectangulo':
#         return(dato['base'*dato['altura']])# si el valor de la clave es 'Rectangulo' imprime el valor de la clave 'base multiplido por la clave 'Altura'
#     elif dato['figura'] == 'Triangulo':
#         return(dato['base']*dato['altura']/2)
#     elif dato['figura'] == 'Circulo':
#         return(3.141593*dato['radio']**2)
#     else:
#         print('Figura desconocida')           

# Triangulo = area(figura = 'Triangulo', base =10, altura =8)
# print(f'El area del triangulo es: {Triangulo}')
# Circulo = area(figura = 'Circulo', radio = 10, color = 'Rojo')  
# print(f'El area del circulo es: {Circulo}')      
# Degocagono =area(figura = 'Degocagono', lado = 10,)
# print(f'El area del degocagono es: {Degocagono}')


##############
# def promedio (*numeros):
#     return sum(numeros)/len(numeros) # con la funcion 'return' el resultado de obtenido en un namespace local se puede utilizar en un ambito global, osea, fuera de la funcion

# x = promedio(4,5,6)
# print(x)    

############3
#Recursividad de funciones en Python
# def factorial(numero):
#     if numero == 0:
#         return 1
#     else:
#         return numero * factorial(numero - 1)
    
# print('El factorial de 0 es (0!): ', factorial(0))
# print('El factorial de 1 es (1!): ', factorial(1))
# print('El factorial de 3 es (3!): ', factorial(3))
# rint('El factorial de -1 es (-1!): ', factorial(-1))

# #########################
# #Funciones lambda o funciones anonimas

# suma =lambda x, y: x + y # en este caso la variable es una funcion a la vez , en la que se definene las variable con la que trabajara y despues de lo s : se indica que operacion realizara
# print('Hola', 'mundo!')
# print(suma(2,5))

# lista_numeros=[1, 0, -2]
# lista_numeros = sorted(lista_numeros) #la funcion "Sorted" la que nos odena alguna lista qeu se le indique
# print(lista_numeros)
# lista_letras=['d','a','g']
# lista_letras = sorted(lista_letras)
# print(lista_letras)
# lista_numeros = sorted(lista_numeros, key= lambda n: abs(n))   

#################
#Funcion zip

paises = ['Kenia','Francia', 'Mexico', 'Japon']
capitales = ['Nairobi', 'Paris', 'Ciudad de Mexico', 'Tokio']
poblacion = [54, 66, 130, ]

for i in zip(paises, capitales, poblacion): #funcion ZIP no sirve para emparejar elementos en mlistas o tuplas o iterables  y respetara la cantidad de elementos de la lista mas pequeña
    print(i)
