import sys
from auxiliares import nombre_aplicacion,version_aplicacion,menu_superior,menu_biblioteca,opcion_invalida,menu_anterior
from presentacion.presentacion_biblioteca import mostrar_paises
from presentacion.presentacion_biblioteca import solicitar_datos_pais

def menu_principal():
    print(f'\n{nombre_aplicacion} - {version_aplicacion}')
    print(f'{'=' * len(nombre_aplicacion)}==={'=' * len(version_aplicacion)}\n')

    while True:
        for clave,valor in menu_superior.items():
            print(f'[{clave}] - {valor}')
        opcion_usuario = input('\nIngrese su opción [1-4]: ')

        match opcion_usuario:
            case '1':
                while True:
                    for numero,nombre in menu_biblioteca.items():
                        print(f'[{numero}] - {nombre}')
                    opcion_sub_menu = input('\nIngrese su opción [0-2]: ')
                    match opcion_sub_menu:
                        case '1':
                            mostrar_paises()
                        case '2':
                            solicitar_datos_pais()
                        case '0':
                            print(menu_anterior)
                            break
                        case _:
                            print(opcion_invalida)
            case '2':
                print('Opción 2')
            case '3':
                print('Opción 3')
            case '0':
                print('Saliendo...')
                sys.exit()
            case _:
                print(opcion_invalida)