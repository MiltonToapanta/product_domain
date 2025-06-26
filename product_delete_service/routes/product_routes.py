from flask import Blueprint, request, jsonify
from __init__ import db
from models.product import Product
from schemas.product_schema import product_schema
#Descomentar para usar validación JWT Token
#from flask_jwt_extended import jwt_required, get_jwt_identity

product_bp = Blueprint("product_bp", __name__)

@product_bp.route("/delete/<int:product_id>", methods=["DELETE"])
#@jwt_required()
def eliminar_producto(product_id):
    producto = Product.query.get(product_id)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404

    db.session.delete(producto)
    db.session.commit()

    return jsonify({"message": f"Producto con id {product_id} eliminado correctamente"}), 200

# Healthcheck route
@product_bp.route("/", methods=["GET"])
def healthcheck():
    return jsonify({"status": "Service is up and running"}), 200
