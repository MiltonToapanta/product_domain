from flask import Blueprint, request, jsonify
from product_add_service import db
from product_add_service.models.product import Product
from product_add_service.schemas.product_schema import product_schema, products_schema

product_bp = Blueprint("product_bp", __name__)

@product_bp.route("/create", methods=["POST"])
def crear_producto():
    data = request.json
    nuevo = product_schema.load(data)
    db.session.add(nuevo)
    db.session.commit()
    return product_schema.jsonify(nuevo), 201

