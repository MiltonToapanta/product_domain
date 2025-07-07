from flask import Blueprint, jsonify
from __init__ import db
from models.product import Product
from schemas.product_schema import products_schema
#Descomentar para usar validación JWT Token
#from flask_jwt_extended import jwt_required, get_jwt_identity

product_bp = Blueprint("product_bp", __name__)

@product_bp.route("/all/asc", methods=["GET"])
def listar_productos_asc():
    productos = Product.query.order_by(Product.precio).all()  # Orden de menor a mayor precio
    return products_schema.jsonify(productos), 200


# Healthcheck route
@product_bp.route("/", methods=["GET"])
def healthcheck():
    return jsonify({"status": "Service is up and running"}), 200