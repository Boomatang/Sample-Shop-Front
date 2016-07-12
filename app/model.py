from datetime import datetime

from flask_login import UserMixin

from . import db, login_manager
from sqlalchemy import ForeignKeyConstraint
from werkzeug.security import generate_password_hash, check_password_hash


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
        return "<Product %s; Name> %s" % (self.proID, self.title)


class Images(db.Model):
    __tablename__ = 'images'
    imgID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    proID = db.Column(db.Integer)
    ForeignKeyConstraint([proID], [Product.proID])
    db.relationship('Product', backref="Images")

    def __repr__(self):
        return "<Image: %s>" % self.name


class Owners(db.Model):
    __tablename__ = 'owners'
    owner_ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    signup_date = db.Column(db.Date)
    confirmed = db.Column(db.Boolean, default=True)
    password_hash = db.Column(db.String(128))
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)

    def __repr__(self):
        return "<User %s, %s>" % (self.ID, self.username)


class Role(db.Model):
    __tablename__ = 'roles'
    ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))