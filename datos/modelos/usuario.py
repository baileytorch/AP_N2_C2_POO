from peewee import Model,SQL,AutoField,CharField,IntegerField,DateField
from datos.conexion import conectar_db
from auxiliares import defecto
database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class Usuario(BaseModel):
    id_usuario = AutoField()
    rut = CharField(max_length=12, null=True, unique=True)
    nombre = CharField(max_length=25)
    apellido = CharField(max_length=25)
    correo = CharField()
    pais = IntegerField(index=True, null=True)
    fecha_nacimiento = DateField(null=True)
    genero = IntegerField()
    fecha_incorporacion = DateField()
    habilitado = IntegerField(constraints=[SQL(defecto)])
    password = CharField(max_length=60)

    class Meta:
            table_name = 'usuarios'