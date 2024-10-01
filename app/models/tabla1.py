from ..extensions import db

class Tabla1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    tabla2_id = db.Column(db.Integer, db.ForeignKey('tabla2.id'), nullable=False)

    def __repr__(self):
        return f"<Tabla1 {self.nombre}>"

    @staticmethod
    def get_by_id(tabla1_id):
        """Obtener un registro por su ID."""
        return Tabla1.query.get(tabla1_id)

    @staticmethod
    def get_all():
        """Obtener todos los registros."""
        return Tabla1.query.all()

    @staticmethod
    def get_by_nombre(nombre):
        """Obtener registros por nombre."""
        return Tabla1.query.filter_by(nombre=nombre).all()
