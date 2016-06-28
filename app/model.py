
from . import db
from sqlalchemy import ForeignKeyConstraint


class Product(db.Model):
    __tablename__ = 'products'
    proID = db.Column(db.Integer, primary_key=True, )
    title = db.Column(db.String(64))
    description = db.Column(db.String)
    cost = db.Column(db.Float)
    default_image_ID = db.Column(db.Integer)
    owner_ID = db.Column(db.Integer)
    available = db.Column(db.Boolean, default=False)
    stock_qty = db.Column(db.Integer)

    def __repr__(self):
        return "Product %s; Name %s" % (self.proID, self.title)


class Images(db.Model):
    __tablename__ = 'images'
    imgID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    proID = db.Column(db.Integer)
    ForeignKeyConstraint([proID], [Product.proID])

    def __repr__(self):
        return "Image: %s" % self.name


class Owners(db.Model):
    __tablename__ = 'owners'
    owner_ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))


class User(db.Model):
    __tablename__ = 'users'

    ID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    emial = db.Column(db.String)
    password = db.Column(db.String)
    signup_date = db.Column(db.Date)

    def __repr__(self):
        return " User %s, %s" % (self.ID, self.username)
