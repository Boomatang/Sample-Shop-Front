from flask import render_template

from . import testing


@testing.route("/")
def testing():

    values = range(0, 8)

    return render_template("main/index.html", list=values)
