import numpy as np

import matplotlib.pyplot as plt  # se llama a libretria la que nos genrara graficas

np.random.seed(0)# esta sentencias  indica qeu el numero random sea constante

numeros = np.random.rand(50)# se genera un numero aleatorio

np.random.normal(media_distribucion, desviacion_estandar, tamaño_de muestras)
print(numeros)

plt.plot(numeros) #se manda a llalos valores de la variable numeros 
plt.show()# muestra valores de numeros en una grafica