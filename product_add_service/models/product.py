from __init__ import db

class Product(db.Model):
    __tablename__ = "productos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255))
    foto = db.Column(db.String(255))  # URL 
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Boolean, default=True)
    categoria = db.Column(db.String(50))
    especie = db.Column(db.Integer)
