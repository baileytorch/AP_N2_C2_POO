from datos.modelos.pais import Pais
from peewee import IntegrityError, OperationalError, DataError, PeeweeException

def listado_paises():
    paises = Pais.select()
    if paises:
        return paises

def guardar_pais(pais:Pais):
    try:
        guardar_pais = pais.save()
        print(guardar_pais)
    except IntegrityError as e:
        print(f"Error de clave unica o clave foránea: {e}")
    except OperationalError as e:
        print(f"Error operacional\n(pérdida de conexión, falta una tabla o base de datos bloqueada): {e}")
    except DataError as e:
        # Handles data values out of range or incorrect formats
        print(f"Valor insertdo NO corresponde: {e}")
    except PeeweeException as e:
        print(f"No se pudieron guardar los datos por un error genérico: {e}")