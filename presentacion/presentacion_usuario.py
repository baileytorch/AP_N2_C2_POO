from negocio.negocio_usuario import lista_usuarios,crear_usuario,actualizar_usuario
from negocio.negocio_pais import buscar_paises
from datos.repositorios.repositorio_paises import obtener_pais_nombre
from prettytable import PrettyTable
from datos.modelos.usuario import Usuario
from auxiliares.mensajes import mensaje_error

def mostrar_usuario():
    try:
        tabla_usuarios = PrettyTable()
        tabla_usuarios = lista_usuarios(tabla_usuarios)
        print(tabla_usuarios)
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')
    

def solicitar_datos_usuario():
    rut = nombre = apellido = correo = pais = id_pais = fecha_nacimiento = genero = contrasenia = ''
    tabla_paises = PrettyTable()
    print('Ingrese Datos de Usuario')
    try:
        while rut == '':
            rut = input('RUT: ')
        while nombre == '':
            nombre = input('Nombre: ')
        while apellido == '':
            apellido = input('Apellido: ')
        while correo == '':
            correo = input('Correo: ')
        while pais == '':
            pais = input('País: ')
            tabla_paises = buscar_paises(tabla_paises, pais)
            print(tabla_paises)
            id_pais = input('ID País:')
        while fecha_nacimiento == '':
            fecha_nacimiento = input('Fecha Nacimiento (dd/mm/yyyy): ')
        while genero == '':
            print('[1] Masculino \n[2] Femenino \n[3]Otro')
            genero = input('Seleccione Género [1-3]: ')
            if genero not in ['1','2','3']:
                genero = ''
        while contrasenia == '':
            contrasenia = input('Contraseña: ')
        
        crear_usuario(rut, nombre, apellido, correo, id_pais, fecha_nacimiento, genero, contrasenia)
    except Exception as error:
        print(f'{mensaje_error} {error}')

def modificar_pais():
    pais_encontrado = Usuario()
    try:
        nombre_pais = ''
        while nombre_pais == '':
            nombre_pais = input('Ingrese nombre país a modificar: ')
            pais_encontrado = obtener_pais_nombre(nombre_pais)
            if pais_encontrado:
                print(f'\nID: {pais_encontrado.id_pais} - Nombre: {pais_encontrado.usuario}')
                print(f'Nacionalidad: {pais_encontrado.nacionalidad} - ISO 2: {pais_encontrado.iso2} - ISO 3: {pais_encontrado.iso3}\n')

                usuario = input('Ingrese nombre país (o ENTER para conservar): ')
                nacionalidad = input('Ingrese nacionalida país (o ENTER para conservar): ')
                iso2 = input('Ingrese ISO 2 país (o ENTER para conservar): ')
                iso3 = input('Ingrese ISO 3 país (o ENTER para conservar): ')
                actualizar_pais(usuario,nacionalidad,iso2,iso3,True,pais_encontrado)
            else:
                nombre_pais = ''
    except Exception as error:
        print(f'{mensaje_error} {error}')

def eliminar_pais():
    pais_encontrado = Usuario()
    try:
        nombre_pais = ''
        while nombre_pais == '':
            nombre_pais = input('Ingrese nombre país a eliminar: ')
            pais_encontrado = obtener_pais_nombre(nombre_pais)
            if pais_encontrado:
                print('Se eliminará el siguiente país:')
                print(f'\nID: {pais_encontrado.id_pais} - Nombre: {pais_encontrado.usuario}')
                print(f'Nacionalidad: {pais_encontrado.nacionalidad} - ISO 2: {pais_encontrado.iso2} - ISO 3: {pais_encontrado.iso3}\n')
                habilitado = False
                actualizar_pais(
                    pais_encontrado.usuario,
                    pais_encontrado.nacionalidad,
                    pais_encontrado.iso2,
                    pais_encontrado.iso3,
                    habilitado,
                    pais_encontrado)
            else:
                nombre_pais = ''
    except Exception as error:
        print(f'{mensaje_error} {error}')