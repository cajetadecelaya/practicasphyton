import random
import matplotlib.pyplot as plt

eje_x = [random.randint(1,100) for n in range(10)] #se genera un alista de 100 elementos que contendra 100 numeros aleatorios generados automaticamente


eje_y = [random.randint(1,100) for n in range(10)]

plt.scatter(eje_x, eje_y) #construye la grafica dde dispersion a partir de los datos infresados

plt.title('Grafica de dispersion')# se asigna nombre a la grafica
plt.show()