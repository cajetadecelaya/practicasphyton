#### los dicionarios pueden conjunto de datos por pares y estos puedes ser ubicados por una llave identificadora
tiempos = {
    'Hamilton': '1:49.9',
    'bottas' : '1:56.4',
    'Perez' : '1:53.8',
    'otro' : '1:52.6'
}

print(tiempos.items())# metodo items permite devolver una lista de tuplas obteniendo la llave y su respectivo valor
print(tiempos.keys()) # metodo  .keys nos muestra un lista con solo las claves de los corredores.
print(tiempos.values()) # metodo .value impreme todos los valores.
print(tiempos.get('otro')) #metodo .get impreme los valores de 'otro'.
print(tiempos.get('Otro', 'no encontrado')) # si se pide un dato y no se encunetra este arrojara el mnesaje de la segunda llave 'No encontrado'

tiempos = dict(  
    Hamilton = '1:49.9',
    Botas = '1:56.4',
    Perez = '1:53.8',
    Otro =  '1:52.6'
) #con la funcion dict nos permite repetir el valor de cada llave

print(tiempos)