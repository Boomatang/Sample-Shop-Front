from flask import render_template
from . import main


@main.route('/')
def index():
    values = range(0, 8)

    return render_template("main/index.html", list=values)


@main.route("/products")
def products():
    values = range(0, 25)

    return render_template("main/products.html", list=values)
