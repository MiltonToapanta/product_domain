from flask import Blueprint, request, jsonify
from __init__ import db
from models.product import Product
from schemas.product_schema import product_schema

product_bp = Blueprint("product_bp", __name__)

@product_bp.route("/delete/<int:product_id>", methods=["DELETE"])
def eliminar_producto(product_id):
    producto = Product.query.get(product_id)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404

    db.session.delete(producto)
    db.session.commit()

    return jsonify({"message": f"Producto con id {product_id} eliminado correctamente"}), 200

