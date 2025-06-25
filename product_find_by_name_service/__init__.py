from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from config import Config
#import os
#Descomentar para usar validación JWT Token
# from flask_jwt_extended import JWTManager

db = SQLAlchemy()
ma = Marshmallow()
#jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    #app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY") 
    #jwt.init_app(app)
    db.init_app(app)
    ma.init_app(app)

    from routes.product_routes import product_bp
    app.register_blueprint(product_bp, url_prefix="/api/products")

    return app
