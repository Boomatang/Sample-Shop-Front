from flask import render_template

from . import testing


@testing.route("/testing")
def testing():
    return render_template("main/contact.html")
