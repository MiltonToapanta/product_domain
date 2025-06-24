from flask import Blueprint, jsonify
from __init__ import db
from models.product import Product
from schemas.product_schema import products_schema

product_bp = Blueprint("product_bp", __name__)

@product_bp.route("/all", methods=["GET"])
def listar_productos():
    productos = Product.query.all()
    return products_schema.jsonify(productos), 200
