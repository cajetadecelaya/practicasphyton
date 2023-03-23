#########Simulación de la Máquina de Galton

import random

import matplotlib.pyplot as plt
def grafica():
     """Se define funcion que se encargara de generar la grafica,incluyendo titulo y nombre de ejes """
     plt.hist(lista_decisiones)
     plt.title('Simulacion de la maquina de Galton') 
     plt.xlabel('Contenedores')
     plt.ylabel('Cantidad de canicas')      
     plt.show()

bola = 3000    
lista_decisiones = [] 
'''Aqui se almacenaran los resultados de la ubicacione final de cada bola'''

for i in range(bola):
    
    def decisiones (num_tiros):
        posicion = 12 
        '''Posicion central en la que iniciaria la bola a caer en el primer nivel.'''
        
        for dado in range(num_tiros):
            rd = int(random.randint(1,2))
            
            if rd <= 1:
                posicion = posicion - 1
                

            elif rd >= 2:
                posicion = posicion + 1
               
        
        
        print(f'Ubicacion final de la pelota {i} se ubica en a casilla :{posicion}') 
        '''Esta imprecion es para poder dar seguimiento al resultado de cada bola'''  

        return posicion
        

    x = decisiones(12)  
    """Aqui defino los niveles, o la cantidad de veces en la que la bola
        tomara la decicion de avanzar o retroceder de ubicacion."""   
    lista_decisiones.append(x)

print(lista_decisiones)
grafica()
    
