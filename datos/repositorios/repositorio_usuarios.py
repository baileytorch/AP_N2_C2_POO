from datos.modelos.usuario import Usuario
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

def listado_usuarios():
    paises = Usuario.select().where(Usuario.habilitado == True)
    if paises:
        return paises

def guardar_usuario(usuario:Usuario):
    try:
        guardar_usuario = usuario.save()
        if guardar_usuario == 1:
            print(f'Usuario guardado con éxito con Id: {Usuario.id_usuario}.')
    except IntegrityError as e:
        print(f"Error de clave unica o clave foránea: {e}")
    except OperationalError as e:
        print(f"Error operacional\n(pérdida de conexión, falta una tabla o base de datos bloqueada): {e}")
    except DataError as e:
        # Handles data values out of range or incorrect formats
        print(f"Valor insertdo NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudieron guardar los datos por un error genérico: {e}")

def obtener_usuario_rut(rut=''):
    if rut != '':
        usuario_encontrado = Usuario.get(Usuario.rut == rut)
    return usuario_encontrado