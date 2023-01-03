

numHuevos = 12
# print('tengo' + numHuevos + 'huevos') # en este ejemplo arrojara un erro debido a que no se puede concatenar un string co un variable por lo que se mostraran 2 opciones para solucionar estes error
 
 #Opcion 1
print('tengo ' + str(numHuevos) + ' huevos.') #La variable se convierte a una cadena para lograr concatenar

#Opcion 2
print('tengo %s huevos.' %(numHuevos)) #Con %s se le indica qu een ese lugra ira ina variable y despues al % se le indicara qu evariable tomara


####
Error de logica
lado = int(input('Ingrese la medida del cuadrado: '))
superficie = lado*lado

print('la superficie del cuadrado es:' + str(superficie))

######
#Ejercicio semana 4
nombre = input('Introduce tu nombre: ')
apellido = input('Intruce tu apellido: ')
edad = int(input('Intruduce tu edad: ')) #La funcion int tranforma la cadena que ingrese el usuario a entero
correo = input('Intruduce el correo elecronico: ')
telefono = input('introduce tu numero de telefono: ')
print('Nombre: ' + nombre)
print('Apellido: ' + apellido)
print('Tengo: ' + str(edad) + ' años')
print('Correo: ' +correo)
print('Telefono: ' + telefono)
