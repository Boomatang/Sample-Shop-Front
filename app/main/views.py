from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

from config import Config
from . import main
from .. import db
from ..functions import get_default_image
from ..model import Product, Images


@main.route('/')
def index():
    values = db.session.query(Product).filter(Product.available == 1).limit(12)
    values = values.all()
    #values = range(0, 8)

    for value in values:
        name = get_default_image(value.default_image_ID)
        value.image = name

    return render_template("main/index.html", list=values)


@main.route("/products")
def products():
    values = db.session.query(Product).filter(Product.available == 1).limit(12)
    values = values.all()
    # values = range(0, 8)

    for value in values:
        name = get_default_image(value.default_image_ID)
        value.image = name

    return render_template("main/products.html", list=values)


@main.route("/contact")
def contact():
    return render_template("main/contact.html")


@main.route("/products/<item>")
def product_view(item):

    product = db.session.query(Product).filter(Product.proID == item).one()

    image_name = get_default_image(product.default_image_ID)
    product.image = image_name

    return render_template("main/product-view.html", product=product)


@main.route("/cart")
def cart():
    values = range(0, 4)
    return render_template("main/cart.html", values=values)


