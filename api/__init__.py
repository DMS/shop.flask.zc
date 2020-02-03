from flask import Flask
from api.plugins import cors, migrate, marshmallow
from api.settings import ProdConfig, DevConfig
from api.cart.routes import carts_blueprint
from api.shipment.routes import shipment_blueprint
from api.products.routes import products_blueprint
from api.user.routes import user_blueprint
from api.commands import seed


def register_plugins(app):
    from api.cart.models import Item, Cart, Order
    from api.shipment.models import Shipment, ShipmentTrack
    from api.products.models import Product, ProductReview, Category, Tag
    from api.user.models import User, Address
    from api.plugins import db
    from api.plugins import cli
    cli.init_app(app)
    db.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)
    marshmallow.init_app(app)


def register_blueprints(app):
    app.register_blueprint(carts_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(products_blueprint)
    app.register_blueprint(shipment_blueprint)


def create_app(config_object=ProdConfig):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config_object.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config_object.SQLALCHEMY_TRACK_MODIFICATIONS
    register_plugins(app)
    register_blueprints(app)
    return app
