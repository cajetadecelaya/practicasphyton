contraseña = input('Ingrese contrasela que inicie con numero:')
if not contraseña[0].isdigit():
    while not contraseña[0].isdigit():
         print('La contresela debe iniciar con numero:')
         contraseña = input('Ingrese contrasela que inicie con numero:')
for i in range(3):
    confirmar= input('Ingrese contrasela nuevamente: ')
    if confirmar!= contraseña:
        print('Las contraseñas no coinciden.')
    else:
        print('Las contraseñas coinciden.')
        break    
print('Fin del programa')
