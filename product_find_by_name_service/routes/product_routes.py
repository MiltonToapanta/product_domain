from flask import Blueprint, request, jsonify
from __init__ import db
from models.product import Product
from schemas.product_schema import products_schema
#Descomentar para usar validación JWT Token
#from flask_jwt_extended import jwt_required, get_jwt_identity

product_bp = Blueprint("product_bp", __name__)

@product_bp.route("/search", methods=["GET"])
#@jwt_required()
def buscar_producto():
    nombre = request.args.get("nombre", "")
    if not nombre:
        return jsonify({"error": "Se requiere el parámetro 'nombre'"}), 400

    resultados = Product.query.filter(Product.nombre.ilike(f"%{nombre}%")).all()
    return products_schema.jsonify(resultados), 200

# Healthcheck route
@product_bp.route("/", methods=["GET"])
def healthcheck():
    return jsonify({"status": "Service is up and running"}), 200