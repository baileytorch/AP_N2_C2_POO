from negocio.negocio_pais import crear_pais

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