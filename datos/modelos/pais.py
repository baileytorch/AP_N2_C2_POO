from peewee import Model,SQL,AutoField,CharField,IntegerField
from datos.conexion import conectar_db

database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class Pais(BaseModel):
    id_pais = AutoField()
    pais = CharField(max_length=50)
    nacionalidad = CharField(max_length=50,null=True)
    iso2 = CharField(max_length=2)
    iso3 = CharField(max_length=3)
    habilitado = IntegerField(constraints=[SQL("DEFAULT 1")])

    class Meta:
        table_name = 'paises'