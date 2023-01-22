# def sumar(parametro1, parametro2):
#     """Funcion que suma dos parametros y los imrpime en pantalla"""
#     print('suma:', parametro1 +parametro2)

# argumento1 = 5
# argumento2 = 7

#invocando a la funcion por medio de parametros variables
#sumar(argumento1,argumento2)

#Invocando a la funcion por medio de parametros de valor
#sumar('mundo!','hola ')


##############33
#Parametros opcionales
def muestra_alumno(nombre, edad =18, sexo= 'F'):
    """Es una funcion qyue muestra en pantalla  el nombre, la edad y el sexo de un alumno
    Recibe tres parametro.
    1. Nombre
    2. Edad =18
    3. Sexo = 'F'"""
    print(f'Nombre: {nombre}, edad: {edad}, sexo: {sexo}')

#Ejecucion de  funcion con parametro obligatorio
muestra_alumno('maria')

#Ejecucion utilizando el parametro obligatorio y un o opcional
muestra_alumno('maria', 22)

#ejecucio de funcion con el primer parametro y  ultimo parametro
muestra_alumno('Juan', sexo= 'M')