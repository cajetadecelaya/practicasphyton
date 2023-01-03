# nomb = input('Mete tu nombre: ')
# while not nomb.isalpha():
#     internto = input('Ingresa caracteres validos: ')
#     if internto.isalpha():
#         nomb = internto
#         break
# print(f'nombre ingresado {nomb}')

edad = int(input('Ingrese su edad en años cumplidos: '))  
if isinstance(edad,int):
    while True:
        print(f"escribiste el numero; {edad}")
        break
elif not isinstance(edad,int):
    intentoe=int(f'Ingresaste algo que no es numero que es:{edad}')


# if nomb.isalpha():    
#     print(nomb)
# elif internto.isalpha():
#     print(internto)


# nomb=input('Mete letras: ')
# if  nomb.isalpha():
#      print("Ok solo tiene letras del alfabeto")
  
# else:
#      print("La tiene caracteres que no son del alfabeto")

##


# ### Multiplicar n cantidad de veces el nombre ingresado
# apellido = input('Escribe tu apellido: ')
# numero = int(input('Escribe un numero: ')) #metodo para nuemros y convertirlo a entero
# print(f'{apellido}\n' *numero) #\n se utiliza para dar un salto de linea. Se imprimira el apellido el numero de veces que indique la variable numero

# ### MOstrar cuantas letras tiene el nombre ingresado
# nombre2 = input('Excribe tu nombre: ')
# print(f'{nombre2} tiene {len(nombre2)} letras') # La funcion 'len' cuenta los espacios utilizados para escribir el nombre

# ### Ejercicio matematico

# print(((3+2) / 2.5)**2)
# operacion = ((3+2) / 2.5)**2
# print(f'E resultado de la operacion es {operacion}')

# #### Relacion horas rabajadas con paga
# horas_trabajadas = int(input('¿Cuantas horas trabajaste: '))
# coste_por_hora = int(input('¿Cuanto cobras por hora: '))
# print(f'El coste del trabajo por {horas_trabajadas} es de ${horas_trabajadas * coste_por_hora}')

# ### Sumas se numero 1 mas el nuemro siguiente la cantidad de veces que ingresemos a la variable n
# n = int(input('Introdusca un numer: '))
# suma = n* (n+1) /2
# print(f'La suma es de 1 hasta {n} es igual a {suma}')

# #### Indice de masa corporal
# peso = float(input('Ingrese su peso en kilogramos: '))
# estatura = float(input('Ingrese su estatura en metro: '))

# imc = (peso / (estatura**2))
# print('Cuenta con un IMC ' +'{:.2f}'.format(imc)) # el resultado de IMC se dedondea a 2 decimales.
# print(f'Tu indice de masa corporal es {round(imc,2)}') #segunda opcion para redondiar decimales.

# ###  Division mostrando resultado y residuo
# n = float(input('Ingresa un numerador: ')) #numerador es el de arriba 
# m = float(input('Ingrese un denominador: ')) #denominador es el de abajo
# c = n/m # arroja el resultado en enteros
# r = n%m # con el %(modulo) nos arroja el residuo
# print(f'El resultado de dividir {n} entre {m} es {round(c,3)} y su residuo es {r}')

# ### tasa de interes y ganancia para invertir

# ci= float(input('Ingresa tu capital inicial: '))
# i = float(input('¿Cual es la tasa de interes? '))
# n = float(input('¿Cuantos años invertiras?'))
# cf = ci * (1+i)**n
# print(f'Con un capital inicial de {ci}, una tasa de interes {i}% e invirtiendo {n} años tu capital final es de ${cf} ')

# ### Peso total de articulos

# payaso = float(112)
# muñeca = float(95)
# payasos_vendidos = int(input('Cuantos payasos fueron vendido? '))
# muñecas_vendidas = int(input('Cuantas muñecas fueron vendidas? '))
# pesos_total = (payaso * payasos_vendidos) + (muñeca * muñecas_vendidas)
# print(f'El peso total de los muñecos y mulecas es: {pesos_total/1000}kg.')

# #### Finanzas calculo de interes por mes
# interes = 0.04
# inversion = float(input('Escribe tu inversion inicical: '))
# balance1 =  inversion * (1+interes) 
# print(f'Despues de un año, tienes {balance1}')
# balance2 = balance1 * (1+interes)
# print(f'Despues de un año, tienes {balance2}')
# balance3 = balance1 * (1+interes)
# print(f'Despues de un año, tienes {balance3}')

# ####  
# coste_barra_pan = 3.49
# descuento = .6
# barras_vendidas = int(input('¿Cuantas barras de pan vendiste? '))
# descuento_pan = barras_vendidas * coste_barra_pan * (1-descuento)
# print(f'El precion con descuento por las barras de pan es de {round(descuento_pan,2)}')


