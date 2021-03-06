from flask import render_template, make_response
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.utils import secure_filename

from config import Config
from . import main
from .. import db
from ..functions import get_default_image, get_products
from ..model import Product, Images


@main.route('/', methods=['POST', 'GET'])
def index():

    return render_template("main/index.html", list=get_products())


@main.route("/products")
def products():

    return render_template("main/products.html", list=get_products())


@main.route("/contact")
def contact():
    return render_template("main/contact.html")


@main.route("/products/<item>")
def product_view(item):

    try:
        product = db.session.query(Product).filter(Product.proID == item).one()

        image_name = get_default_image(product.default_image_ID)
        product.image = image_name

        return render_template("main/product-view.html", product=product)
    except NoResultFound:
        response = make_response(render_template('errors/404.html'), 404)

        return response


@main.route("/cart")
def cart():
    values = range(0, 4)
    return render_template("main/cart.html", values=values)


