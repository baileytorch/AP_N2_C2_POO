from negocio.negocio_pais import lista_paises,crear_pais,actualizar_pais
from datos.repositorios.repositorio_paises import obtener_pais
from prettytable import PrettyTable
from datos.modelos.pais import Pais
from auxiliares.mensajes import mensaje_error

def mostrar_paises():
    try:
        # Instancia de la clase PrettyTable
        tabla_paises = PrettyTable()
        tabla_paises.field_names = ['Id','País','Nacionalidad','ISO 2','ISO 3','Habilitado']
        tabla_paises = lista_paises(tabla_paises)
        print(tabla_paises)
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')
    

def solicitar_datos_pais():
    pais = nacionalidad = iso2 = iso3 = ''
    try:
        while pais == '':
            pais = input('Ingrese nombre país: ')
        while nacionalidad == '':
            nacionalidad = input('Ingrese nacionalida país: ')
        while iso2 == '':
            iso2 = input('Ingrese ISO 2 país: ')
        while iso3 == '':
            iso3 = input('Ingrese ISO 3 país: ')
        
        crear_pais(pais, nacionalidad, iso2, iso3)
    except Exception as error:
        print(f'{mensaje_error} {error}')

def modificar_pais():
    pais_encontrado = Pais()
    try:
        nombre_pais = ''
        while nombre_pais == '':
            nombre_pais = input('Ingrese nombre país a modificar: ')
            pais_encontrado = obtener_pais(nombre_pais)
            if pais_encontrado:
                print(f'\nID: {pais_encontrado.id_pais} - Nombre: {pais_encontrado.pais}')
                print(f'Nacionalidad: {pais_encontrado.nacionalidad} - ISO 2: {pais_encontrado.iso2} - ISO 3: {pais_encontrado.iso3}\n')

                pais = input('Ingrese nombre país (o ENTER para conservar): ')
                nacionalidad = input('Ingrese nacionalida país (o ENTER para conservar): ')
                iso2 = input('Ingrese ISO 2 país (o ENTER para conservar): ')
                iso3 = input('Ingrese ISO 3 país (o ENTER para conservar): ')
                actualizar_pais(pais,nacionalidad,iso2,iso3,True,pais_encontrado)
            else:
                nombre_pais = ''
    except Exception as error:
        print(f'{mensaje_error} {error}')

def eliminar_pais():
    pais_encontrado = Pais()
    try:
        nombre_pais = ''
        while nombre_pais == '':
            nombre_pais = input('Ingrese nombre país a eliminar: ')
            pais_encontrado = obtener_pais(nombre_pais)
            if pais_encontrado:
                print('Se eliminará el siguiente país:')
                print(f'\nID: {pais_encontrado.id_pais} - Nombre: {pais_encontrado.pais}')
                print(f'Nacionalidad: {pais_encontrado.nacionalidad} - ISO 2: {pais_encontrado.iso2} - ISO 3: {pais_encontrado.iso3}\n')
                habilitado = False
                actualizar_pais(
                    pais_encontrado.pais,
                    pais_encontrado.nacionalidad,
                    pais_encontrado.iso2,
                    pais_encontrado.iso3,
                    habilitado,
                    pais_encontrado)
            else:
                nombre_pais = ''
    except Exception as error:
        print(f'{mensaje_error} {error}')