##########Longuitud de una frase

palabra = input('Ingrese una palabra que contenga entre 4 y 8 letras: ')

if len(palabra) > 3:
        if len(palabra) <9:
            print('La palabra es correcta')
            exit()
        else:
            print(f'Sobran letras. Tienes {len(palabra)} letras.') 
            palabra = input('Ingrese una palabra que contenga entre 4 y 8 letras: ')

elif len(palabra) <4:
        print(f'Hacen falta letras. Tienes {len(palabra)} letras')      
        palabra = input('Ingrese una palabra que contenga entre 4 y 8 letras: ')

########Encuentra el cuadrante
while True:
    try:
        x = int(input('Ingrese X: '))
        if x !=0:
            break
        else:
            print('Valor a 0 no es permitido!')

    except ValueError:
        print('Dato invalido.')  

while True:
    try:
        y = int(input('Ingrese Y: '))
        if y !=0:
         break
        else:
           print('Valor a 0 no es permitido!') 

    except ValueError:
         print('Dato invalido.')   

if x >0 and y >0:
    print('El punto se encuentra en el cuadrante 1')
elif x < 0 and y> 0:
    print('El punto se encuentra en el cuadrante 2')
elif x < 0 and y < 0:  
    print('El punto se encuentra en el cuadrante 3') 
elif x > 0 and y < 0:  
    print('El punto se encuentra en el cuadrante 4') 
