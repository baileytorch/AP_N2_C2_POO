from negocio.negocio_pais import lista_paises,crear_pais
from prettytable import PrettyTable

def mostrar_paises():
    # Instancia de la clase PrettyTable
    tabla_paises = PrettyTable()
    tabla_paises.field_names = ['Id','País','Nacionalidad','ISO 2','ISO 3','Habilitado']
    tabla_paises = lista_paises(tabla_paises)
    print(tabla_paises)

def solicitar_datos_pais():
    pais = nacionalidad = iso2 = iso3 = ''

    while pais == '':
        pais = input('Ingrese nombre país: ')
    while nacionalidad == '':
        nacionalidad = input('Ingrese nacionalida país: ')
    while iso2 == '':
        iso2 = input('Ingrese ISO 2 país: ')
    while iso3 == '':
        iso3 = input('Ingrese ISO 3 país: ')

    crear_pais(pais, nacionalidad, iso2, iso3)