from flask import Blueprint, request, jsonify
from __init__ import db
from models.product import Product
from schemas.product_schema import product_schema, products_schema
#Descomentar para usar validación JWT Token
#from flask_jwt_extended import jwt_required, get_jwt_identity


product_bp = Blueprint("product_bp", __name__)

@product_bp.route("/create", methods=["POST"])
#@jwt_required()
def crear_producto():
    data = request.json
    nuevo = product_schema.load(data)
    db.session.add(nuevo)
    db.session.commit()
    return product_schema.jsonify(nuevo), 201


# Healthcheck route
@product_bp.route("/", methods=["GET"])
def healthcheck():
    return jsonify({"status": "Service is up and running"}), 200
