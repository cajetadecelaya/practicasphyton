





import random

import matplotlib.pyplot as plt

def decisiones (num_tiros):
    posicion = 6
    print(posicion)
    #lista_decisiones = []
    for dado in range(num_tiros):
        rd = int(random.randint(1,2))
        #posicion + rd
        
        if rd <= 1:
         posicion = posicion - 1
         #print(posicion)
         print(f'tiro {dado + 1}, posicion actual {posicion}')
        elif rd >= 2:
         posicion = posicion + 1
         print(f'tiro {dado + 1}, posicion actual {posicion}')
    #lista_decisiones.append(posicion)
    
    print(f'Ubicacion final de la pelota 1 se ubica en a casilla :{posicion}')
    return posicion
    

x = decisiones(2)
print(x)
lista_decisiones = []
lista_decisiones.append(x)
#pelotas(3000)

print(lista_decisiones)

#print(f'El dato dio: {str(random.randint(1, 6))} ')

#plt.hist(str(random.randint(1,2)))
#plt.show()