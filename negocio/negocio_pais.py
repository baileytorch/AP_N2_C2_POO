from datos.repositorios.repositorio_paises import listado_paises,guardar_pais
from prettytable import PrettyTable
from datos.modelos.pais import Pais
from auxiliares.mensajes import mensaje_error


def lista_paises(tabla_paises:PrettyTable):
    paises = listado_paises()
    if paises:
        for pais in paises:
            tabla_paises.add_row([pais.id_pais, pais.pais, pais.nacionalidad, pais.iso2, pais.iso3, ('Deshabilitado', 'Habilitado')[pais.habilitado]])
        return tabla_paises

def crear_pais(pais, nacionalidad, iso2, iso3):
    nuevo_pais = Pais()
    try:
        nuevo_pais.pais = pais
        nuevo_pais.nacionalidad = nacionalidad
        nuevo_pais.iso2 = iso2
        nuevo_pais.iso3 = iso3
        guardar_pais(nuevo_pais)
    except Exception as error:
        print(f'{mensaje_error} {error}')

def actualizar_pais(nombre_pais, nacionalidad, iso2, iso3, habilitado, pais:Pais):
    try:
        if nombre_pais != '':
            pais.pais = nombre_pais
        if nacionalidad != '':
            pais.nacionalidad = nacionalidad
        if iso2 != '':
            pais.iso2 = iso2
        if iso3 != '':
            pais.iso3 = iso3
        if habilitado != None:
            pais.habilitado = False
        guardar_pais(pais)
    except Exception as error:
        print(f'{mensaje_error} {error}')