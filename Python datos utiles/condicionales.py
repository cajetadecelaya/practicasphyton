# ###  Programa que pregunte edad e indiue si es mayor de edad o no


# if edad >= 18:
#     print('Ustede es mayor de edad')

# else:
#     print('Ustede es menor de edad')

# ###   Almacene contraseña  en una variable verificar coincidencia de contraseeñas

# contraseña = 'contra'
# password = input('Cuall es tu contraseña: ')

# password = password.lower()

# if contraseña == password:
#     print('Bienvenido')

# else:
#     print(f'su password {password} no es similar a la contraseña {contraseña}')

# ###

# numerador = int(input('Escribe un numerador: '))
# denominador = int(input('Escribe un denominador: '))

# if denominador == 0:
#     print('Error! No puedes dividir entre cero')
# else:
#     print(f'La division de numerado {numerador}  entre denominador {denominador} es {round(numerador/denominador,3)} ')

# ###  Pide a ussuario numero entero y muestre si es par o impar

# numero_entero = int(input('Ingrese numero: '))

# if numero_entero % 2 == 0:   #de esta manero le decimos al programa qu ees numero ingresado es numero par
#     print(f'El numero {numero_entero} es par')
# else:
#     print(f'El numero {numero_entero} es impar')

# ###

# edad = int(input('Ingrese su edad: '))
# ingreso = float(input('Ingrese su ingreso: '))

# if edad >15 and ingreso >999:
#     print(f'Ustede debe tributar ya que tiene {edad} y una persepcion de {ingreso}')

# else:
#     print('hagase concha y no pague nada')

# #### Separar por gropos segun su mobre y sexo
# nombre = input('Ingrese su nombre: ')
# sexo = input('Ingrese su sexo: (H o M): ')
# grupo = ''  # se deja la cadena varia para poder asignarle valor mas adelante.

# if ((nombre.lower() < 'm' and sexo =='M') or (nombre.lower() > 'n' and sexo =='H')):
#     grupo = 'a'

# else:
#     grupo = 'b'

# print(f'{nombre} perteneces al grupo {grupo} ')

# ###
# renta = float(input('Ingrese el monto de su renta anual:'))

# if renta <= 10000:
#     print(f'Su renta con el monto de {renta} pagara un impuesto del 5%')
# elif renta >10000 and renta <= 20000:
#     print(f'Su renta con el monto de {renta} pagara un impuesto del 15%')
# elif renta >20000 and renta <= 35000:
#     print(f'Su renta con el monto de {renta} pagara un impuesto del 20%')
# elif renta >35000 and renta <= 60000:
#     print(f'Su renta con el monto de {renta} pagara un impuesto del 30%')
# elif renta >60000:
#     print(f'Su renta con el monto de {renta} pagara un impuesto del 45%')

# ####

# puntuacion = float(input('Escribe tu puntuacion: '))
# sueldo_base = 2400
# benecifio = (puntuacion * sueldo_base) + sueldo_base
# nivel =''
# if puntuacion == 0 or puntuacion == 0.0:
#     nivel = 'inaceptable'
#     print(f'Tu puntuacion es de ${benecifio} y tienes un nivel de {nivel}')
# elif puntuacion == 0.4:
#     nivel = 'aceptable'
#     print(f'Tu puntuacion es de ${benecifio} y tienes un nivel de {nivel}')
# elif puntuacion >= 0.6:
#     nivel = 'meteorito'
#     print(f'Tu puntuacion es de ${benecifio} y tienes un nivel de {nivel}')

# ####

# edad = int(input('Ingrese su edad: '))
# precio_entrada =.0

# if edad < 4:
#     precio_entrada =.0
#     print(f'Tienes entrada gratis por lo que pagas {precio_entrada}')
# elif edad >= 4 and edad < 18:
#     precio_entrada = 5
#     print(f'Ya estas grandecito asi que pagas {precio_entrada}')
# elif edad >= 10:
#     precio_entrada = 10
#     print(f'Ya tienes para pagar asi que pagas {precio_entrada}')

# ###
# pizza =int(input("Escoge un tipo de pizza; 1 para vegetariana y 2 para no vegetariana: "))

# opcion_de_ingredientes = 0

# if pizza == 1:
#     opcion_de_ingredientes = int(input("Escoge un ingrediente: 1 pimineto, 2 toffu: "))
#     if opcion_de_ingredientes == 1:
#          print('Tu pizza es vegetriana y tiene mozzarella, tomate y pimiento')
#     elif opcion_de_ingredientes == 2:
#           print('Tu pizza es vegetriana y tiene mozzarella, tomate y tofu')
#     else:
#         print('Opcion no valida')

# elif pizza == 2:
#     opcion_de_ingredientes = int(input(('Escoge un ingrediente: 1 Peperono, 2 jamon y 3 Salmon')) )
#     if opcion_de_ingredientes == 1:
#          print('Tu pizza es carnivora y contiene mozzarella, tomate y Peperoni')
#     elif opcion_de_ingredientes == 2:
#         print('Tu pizza es carnivora y contiene mozzarella, tomate y jamon')
#     elif opcion_de_ingredientes == 3:
#          print('Tu pizza es carnivora y contiene mozzarella, tomate y salmon')
#     else:
#      print('Opcion no valida')

