from datos.repositorios.repositorio_paises import listado_paises
from prettytable import PrettyTable

def lista_paises():
    # Instancia de la clase PrettyTable
    tabla_paises = PrettyTable()
    tabla_paises.field_names = ['Id','País','Nacionalidad','ISO 2','ISO 3']

    paises = listado_paises()
    if paises:
        for pais in paises:
            tabla_paises.add_row([pais.id_pais, pais.pais, pais.nacionalidad, pais.iso2, pais.iso3])
        print(tabla_paises)
