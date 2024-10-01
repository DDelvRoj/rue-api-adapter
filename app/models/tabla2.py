from ..extensions import db

class Tabla2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(120), nullable=False)
    tabla3_id = db.Column(db.Integer, db.ForeignKey('tabla3.id'), nullable=False)
    def __repr__(self):
        return f"<Tabla2 {self.descripcion}>"