from ..models import Tabla1,Tabla2,Tabla3
from ..extensions import db


def procesar_formulario(nombre, descripcion, detalle):
    try:
        nueva_tabla3 = Tabla3(detalle=detalle)
        db.session.add(nueva_tabla3)
        db.session.commit()

        nueva_tabla2 = Tabla2(descripcion=descripcion, tabla3_id=nueva_tabla3.id)
        db.session.add(nueva_tabla2)
        db.session.commit()

        nueva_tabla1 = Tabla1(nombre=nombre, tabla2_id=nueva_tabla2.id)
        db.session.add(nueva_tabla1)
        db.session.commit()
    except Exception as e:
        db.session.rollback()  # Deshacer cambios en caso de error
        print(f"Error al procesar el formulario: {e}")

# Crear
def crear_tabla1(nombre, tabla2_id):
    nueva_tabla1 = Tabla1(nombre=nombre, tabla2_id=tabla2_id)
    db.session.add(nueva_tabla1)
    db.session.commit()
    return nueva_tabla1

# Leer
def obtener_tabla1_por_id(tabla1_id):
    return Tabla1.query.get(tabla1_id)

def obtener_todos_tabla1():
        return (
        db.session.query(Tabla1, Tabla2, Tabla3)
        .join(Tabla2, Tabla1.tabla2_id == Tabla2.id)
        .join(Tabla3, Tabla2.tabla3_id == Tabla3.id)
        .all()
    )




# Eliminar
def eliminar_tabla1(tabla1_id):
    tabla1 = Tabla1.query.get(tabla1_id)
    if not tabla1:
        return None

    db.session.delete(tabla1)
    db.session.commit()
    return tabla1
