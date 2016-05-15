from flask import render_template

from . import testing


@testing.route("/")
def testing():
    return render_template("base/base.html")
