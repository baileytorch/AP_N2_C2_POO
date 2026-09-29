import sys
from auxiliares import nombre_aplicacion,version_aplicacion,menu_superior,menu_biblioteca

def menu_principal():
    print(f'\n{nombre_aplicacion} - {version_aplicacion}')
    print(f'{'=' * len(nombre_aplicacion)}==={'=' * len(version_aplicacion)}\n')

    while True:
        for clave,valor in menu_superior.items():
            print(f'[{clave}] - {valor}')
        opcion_usuario = input('\nIngrese su opción [1-4]: ')

        if opcion_usuario == '1':
            for numero,nombre in menu_biblioteca.items():
                print(f'[{numero}] - {nombre}')
        elif opcion_usuario == '2':
            print('Opción 2')
        elif opcion_usuario == '3':
            print('Opción 3')
        elif opcion_usuario == '0':
            print('Saliendo...')
            sys.exit()
        else:
            print('Opción ingresada NO corresponde...\nIngrese nuevamente')