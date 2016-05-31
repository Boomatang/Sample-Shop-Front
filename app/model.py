
from . import db


class Product(db.Model):
    __tablename__ = 'products'
    proID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Column(db.String(64))
    description = db.Column(db.text())
    cost = db.Column(db.Integer)
    default_image_ID = db.Column(db.Integer)
    owner_ID = db.Column(db.Integer)
    available = db.Column(db.Boolean, default=False)
    stock_qty = db.Column(db.Integer)


class Images(db.Model):
    __tablename__ = 'images'
    imgID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    proID = db.Column(db.Integer)

class Owners(db.Model):
    __tablename__ = 'owners'
    owner_ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Column(db.String(64))
