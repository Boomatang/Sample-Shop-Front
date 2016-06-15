import os
from flask import render_template, request, redirect, url_for, flash
from flask_uploads import UploadSet, IMAGES
from werkzeug.utils import secure_filename

from config import Config
from . import main

photos = UploadSet('photos', IMAGES)


@main.route('/')
def index():
    values = range(0, 8)

    return render_template("main/index.html", list=values)


@main.route("/products")
def products():
    values = range(0, 25)

    return render_template("main/products.html", list=values)


@main.route("/contact")
def contact():
    return render_template("main/contact.html")


@main.route("/products/<item>")
def product_view(item):
    return render_template("main/product-view.html")


@main.route("/cart")
def cart():
    values = range(0, 4)
    return render_template("main/cart.html", values=values)


@main.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return filename
    return '''
    <html>
    <head>
    <title>Uploads</title>
    </head>
    <body>
    <form method=POST enctype=multipart/form-data action="/upload">
        <input type="file" name="photo">
        <input type="submit">
    </form>
    </body>
    </html>
    '''


