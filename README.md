# AP_N2_C2_POO
Proyecto de desarrollo modular con POO

El desarrollo modular de software es una técnica que divide un programa grande en partes pequeñas e independientes llamadas módulos. Cada módulo cumple una sola tarea específica y se conecta con los demás mediante reglas claras, lo que hace que el sistema sea más fácil de crear, arreglar y crecer con el tiempo.

Principios Clave - Módulos independientes: Bloques de código separados que hacen una sola parte del trabajo. - Interfaces claras: Reglas fijas para que los módulos hablen entre sí sin enredarse. - Alta cohesión: Cada parte se concentra en su propia tarea y la hace muy bien. - Bajo acoplamiento: Los cambios en un módulo no dañan el resto del programa.

Ventajas Principales - Mantenimiento fácil: Es rápido hallar y corregir fallas en una sola parte pequeña. - Trabajo en equipo: Varios grupos pueden crear módulos distintos al mismo tiempo. - Reutilización: Las partes ya hechas sirven para otros proyectos futuros. - Crecimiento simple: Se pueden añadir funciones nuevas sin rehacer todo el sistema.
___

Instalación ORM + Driver de base de datos
```
pip install peewee pymysql
```

Creacion de modelo de forma automatica:
```
python -m pwiz -e mysql -H localhost -p 3306 -u your_username -P your_database_name > models.py
```
