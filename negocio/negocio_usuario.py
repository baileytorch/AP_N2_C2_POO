from datos.repositorios.repositorio_usuarios import listado_usuarios,guardar_usuario
from prettytable import PrettyTable
from datos.modelos.usuario import Usuario
from auxiliares.mensajes import mensaje_error
from datetime import datetime


def lista_usuarios(tabla_usuarios:PrettyTable):
    usuarios = listado_usuarios()
    tabla_usuarios.field_names = ['Id','RUT','Nombre Completo','Correo','Fecha Nacimiento','Género']
    if usuarios:
        for usuario in usuarios:
            nombre_completo = f'{usuario.nombre} {usuario.apellido}'
            tabla_usuarios.add_row([usuario.id_usuario, usuario.rut, nombre_completo, usuario.correo, usuario.fecha_nacimiento, usuario.genero])
        return tabla_usuarios

def crear_usuario(str_rut, str_nombre, str_apellido, str_correo, str_pais, str_fecha_nacimiento, str_genero, str_contrasenia):
    nuevo_usuario = Usuario()
    try:
        nuevo_usuario.rut = str_rut
        nuevo_usuario.nombre = str_nombre
        nuevo_usuario.apellido = str_apellido
        nuevo_usuario.correo = str_correo
        nuevo_usuario.pais = int(str_pais)
        nuevo_usuario.fecha_nacimiento = datetime.strptime(str_fecha_nacimiento, '%d/%m/%Y')
        # nuevo_usuario.fecha_nacimiento = str_fecha_nacimiento
        nuevo_usuario.genero = int(str_genero)
        nuevo_usuario.password = str_contrasenia
        nuevo_usuario.fecha_incorporacion = datetime.now()
        nuevo_usuario.habilitado = True

        guardar_usuario(nuevo_usuario)
    except Exception as error:
        print(f'{mensaje_error} {error}')

def actualizar_usuario(nombre_pais, nacionalidad, iso2, iso3, habilitado, usuario:Usuario):
    try:
        if nombre_pais != '':
            usuario.Usuario = nombre_pais
        if nacionalidad != '':
            usuario.nacionalidad = nacionalidad
        if iso2 != '':
            usuario.iso2 = iso2
        if iso3 != '':
            usuario.iso3 = iso3
        if habilitado != None:
            usuario.habilitado = False
        guardar_usuario(usuario)
    except Exception as error:
        print(f'{mensaje_error} {error}')