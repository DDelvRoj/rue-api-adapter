from ..extensions import db


class Tabla3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    detalle = db.Column(db.String(120), nullable=False)
    def __repr__(self):
     return f"<Tabla3 {self.detalle}>"