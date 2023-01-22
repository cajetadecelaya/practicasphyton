
aactual = int(input('Ingrese año actual: '))
aaleatorio = int(input('Ingrese año aleatorioa para calcular: '))


if aactual > aaleatorio:
    restaact = (aactual - aaleatorio)
    if restaact > 1:
        print (f'Han pasado {restaact} años desde el año que has introducido.')
    else:
        print(f'Desde el año {aaleatorio}  ha pasado 1 año')

elif aactual < aaleatorio:
    restalea = (aaleatorio - aactual)
    if restalea > 1:
        print(f'Faltan {restalea} años para llegar al año que has introducido.')
    else:
        print(f'Para llegar al {aaleatorio} hace falta 1 año.')    

elif aactual==aaleatorio:
    print('¡Has introducido el mismo año que el actual!')          

