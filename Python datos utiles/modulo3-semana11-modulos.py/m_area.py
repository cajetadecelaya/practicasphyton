####Modulo m_area (m_area.py)
"""Modulo que contiene la funcion area"""

def area (**dato):
    """REcibe como parametro un diccionario de un  figura
    Calcula el area de la figura"""

    if dato['figura'] == 'Rectangulo':
        print(dato['base'*dato['altura']])# si el valor de la clave es 'Rectangulo' imprime el valor de la clave 'base multiplido por la clave 'Altura'
    elif dato['figura'] == 'Triangulo':
        print(dato['base']*dato['altura']/2)
    elif dato['figura'] == 'Circulo':
        print(3.141593*dato['radio']**2)
    else:
        print('Figura desconocida')           

