from flask import Blueprint, jsonify
from __init__ import db
from models.product import Product
from schemas.product_schema import products_schema
#Descomentar para usar validación JWT Token
#from flask_jwt_extended import jwt_required, get_jwt_identity

product_bp = Blueprint("product_bp", __name__)

@product_bp.route("/all", methods=["GET"])
#@jwt_required()
def listar_productos():
    productos = Product.query.all()
    return products_schema.jsonify(productos), 200


