# cuadrados = []

# for numero in range(10):
#     numero = numero**2
#     cuadrados.append(numero)
# print(cuadrados)   

# cubos =[cubo **3 for cubo in range(10)]
# print(cubos)

#ejemplo de diccionarios por medio de las compresion de listas

# cubos ={numero : numero **3 for numero in range (10)}
# print(cubos)

# ##### condicionales 

# pares =[numero for numero in range(1,11) if numero % 2 ==0] # genera lista con los numeros pares qu eeste dentro de 11
# impares =[numeros for numeros in range(1,11) if numeros % 2 ==1] #genera lista con los numeros impares qu eeste dentro de 11
# print(pares)
# print(impares)

nombres = ['ana','fernando','carlos','pricila']
print(nombres)
nombres = [nombre.capitalize() for nombre in nombres]# Aqui sobre escribimos lista con primera letra en mayuscula
print(nombres)