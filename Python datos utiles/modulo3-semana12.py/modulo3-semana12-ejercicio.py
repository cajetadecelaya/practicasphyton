import matplotlib.pyplot as plt


def daigrama_barras_calificaciones(notas, color, alumno):
    """Dibujar grafica de barras con las calificaciones"""

    plt.hist(notas.keys(), notas.values(), color = color)
    plt.title(f'Calilficaciones de {alumno}')

calificaciones = {'programacion':9, 
                  'Español':6.5,
                  'Calculo': 4,
                  'Historia':8,
                  'Biologia' :10 }

alumno = "morro" #input('Nombre del alumno: ')
daigrama_barras_calificaciones(calificaciones, 'purple', alumno)
plt.show()