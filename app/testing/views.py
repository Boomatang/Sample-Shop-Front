from flask import render_template

from . import testing


@testing.route("/testing")
def testing():

    values = range(0, 25)

    return render_template("main/products.html", list=values)
