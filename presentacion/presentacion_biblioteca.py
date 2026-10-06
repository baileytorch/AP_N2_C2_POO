from negocio.negocio_pais import crear_pais

def solicitar_datos_pais():
    pais = input('Ingrese nombre país: ')
    nacionalidad = input('Ingrese nacionalida país: ')
    iso2 = input('Ingrese ISO 2 país: ')
    iso3 = input('Ingrese ISO 3 país: ')
    crear_pais(pais, nacionalidad, iso2, iso3)