##Parametros de tipo tupla, *args, 1 * para tipo tupla

def promedio (*numeros): # el * nos indica que podra recibir varios de estos valores
    """Recibe un solo parametro de tipo tupla de valores numericos
    e imprime su promedio"""
    promedio = sum(numeros) / len(numeros)
    print('El promedio es:', promedio)

promedio(4)  
promedio(4,5,6)
promedio(1,2,3,4,5,6,7,8,9)    

def es_numero(titulo, *serie):
    """Imprime un  ttitulo y verifica que el caracter en el parametro de tipo tupla es un nuero o no"""
    print(titulo)
    for i in serie:
        if type(i) == int or i.isdigit():
            print(f'{i} es numero')
        else:
            print(f'{i} no es numero')

es_numero('numero', '1','2','3') 
es_numero('Letras', 'a', 'b','c')     


nombre = 'Mezcla'
lista_varios = ['a','2', 3, 'f', 5]
es_numero(nombre, *lista_varios)


#######################33
#Parametros tipo diccionario ##kwarg, 2 * para tipo diccionario

def area(**dato): # dato es una variable que recibe un diccionario
    """Calcula es alrea de una fgura geometrica y la impprime en pantalla"""
    #si el diccionario tiene una clave llamada 'figura' evalua el valir de la clave
    if dato['figura'] == 'Rectangulo':
        print(dato['base'*dato['altura']])# si el valor de la clave es 'Rectangulo' imprime el valor de la clave 'base multiplido por la clave 'Altura'
    elif dato['figura'] == 'Triangulo':
        print(dato['base']*dato['altura']/2)
    elif dato['figura'] == 'Circulo':
        print(3.141593*dato['radio']**2)
    else:
        print('Figura desconocida')           

area(figura = 'Triangulo', base =10, altura =5)
area(figura = 'Circulo', radio = 10, color = 'Rojo')        
area(figura = 'Degocagono', lado = 10,)