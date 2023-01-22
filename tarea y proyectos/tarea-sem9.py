abecedario = []
def abc(): 
    """Se genera cadenan cadenas  que incluyen el abecedario y se almacenan en una lista"""
    import string
    #print("Alfabeto de la A - Z:")
    for letter in string.ascii_uppercase:
        #print(letter, end=' ')
        abecedario.append(letter)
    #print(abecedario)


###}Bucle infinito.
while True:
    try:
        letra_alfabeto = input('Ingrese letra del alfabeto o escriba Salir para concluir el programa: ').capitalize()
        print(letra_alfabeto)
        
        if letra_alfabeto != 'Salir':
            abc()
            for i in range(len(abecedario)):
                
                if abecedario[i] == letra_alfabeto:
                    print(f'letra alfabeto ingresada {letra_alfabeto}')
                    print(f'Letra anterior {abecedario[i+1]} y letra posterior {abecedario[i-1]}')
                    break
                    
                                        
                # elif abecedario != letra_alfabeto:
                #     print(f'Buscando coincidencias de {letra_alfabeto} con {abecedario[i]}, valor de i {i} ')

                elif letra_alfabeto == 'Salir':
                    break  
        else:
            print('Salir del programa')
            exit()        


    except ValueError:
        print('pendiente')