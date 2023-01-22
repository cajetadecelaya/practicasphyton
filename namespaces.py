#Probando ambitos

titulo = 'Probando ambitos'
suma = 10.5

def sumar():
    suma =2 + 2
    print(titulo)
    print('Suma en ambito local', suma, id(suma))

print('Antes de llamar a la funcion')
print('Suma en ambito global', suma, id(suma))
sumar() #se llama a la funcion sumar antes dedefinida
print('Despues de llamar a la funcion sumar')
print('Suma en ambito global', suma, id(suma))