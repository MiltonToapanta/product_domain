from flask import Blueprint, request, jsonify
from __init__ import db
from models.product import Product
from schemas.product_schema import products_schema

product_bp = Blueprint("product_bp", __name__)

@product_bp.route("/search", methods=["GET"])
def buscar_producto():
    nombre = request.args.get("nombre", "")
    if not nombre:
        return jsonify({"error": "Se requiere el parámetro 'nombre'"}), 400

    resultados = Product.query.filter(Product.nombre.ilike(f"%{nombre}%")).all()
    return products_schema.jsonify(resultados), 200
