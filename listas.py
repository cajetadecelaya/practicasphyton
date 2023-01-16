### saber el tipo de elemento que contiene una lista
# mix = [0, 1.2, 'mono',8/3j]

# # for i in mix:
#     print(f'{i:6} - tipo: {type(i)}')

# #    Imprimircantidad de elementos en la lista

# print(len(mix))

#     Imprimri solo los primeros dos elementos de la lista
# sin_dos= mix[:2] #[:2] indica se contemplara los primeros dos elementos a partir del inicio
# print(mix[2:] + mix[1:2]) #['mono', -2.6666666666666665j, 1.2]

# ###cuadrados
cuadrados = [0,1,4,9,16,25] #se definene los elementos que contiene la lista
for i in range(len(cuadrados)): #for de repetirar el numero veces  en la cantidad de elementos de la lista
    print(f'{i}**2 = {cuadrados[i]}') #Imprimira cada elemento de la lista elevado al cuadrado

    cuadrados.append(7**3)# esta funcion inserta un elemento a lo ultimo de la lista
    
    print(cuadrados)
    cuadrados.insert(6,6**3) #Indicamos que en la posicion 6 se insertara la operacion 6 al cubo
    print(cuadrados)
    cuadrados.extend([27,1000,-1])# ingresamos los tres valores a la tabla cuadrados
    print(cuadrados)
    cuadrados.extend(range(-1,-4,-1))# inserta con un rango ()
    print(cuadrados)
    del cuadrados[9:] #elimina los registros de la tabla del noveno en adelante
    print(cuadrados)
    cuadrados.remove(216)# elimina los registros co el valor 216 que se encuentre en la lista
    print(cuadrados)
    cuadrados.pop(2)#remueve elemento ubicado en el indice 2
    print(cuadrados)
    cuadrados.clear()
    print(cuadrados)
