from flask import Blueprint, request, jsonify
from __init__ import db
from models.product import Product
from schemas.product_schema import product_schema
#Descomentar para usar validación JWT Token
#from flask_jwt_extended import jwt_required, get_jwt_identity

product_bp = Blueprint("product_bp", __name__)

@product_bp.route("/update/<int:product_id>", methods=["PUT"])
#@jwt_required()
def actualizar_producto(product_id):
    producto = Product.query.get(product_id)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404

    data = request.json
    
    if "nombre" in data:
        producto.nombre = data["nombre"]
    if "descripcion" in data:
        producto.descripcion = data["descripcion"]
    if "foto" in data:
        producto.foto = data["foto"]
    if "precio" in data:
        producto.precio = data["precio"]
    if "stock" in data:
        producto.stock = data["stock"]
    if "categoria" in data:
        producto.categoria = data["categoria"]
    if "especie" in data:
        producto.especie = data["especie"]

    db.session.commit()

    return product_schema.jsonify(producto), 200
