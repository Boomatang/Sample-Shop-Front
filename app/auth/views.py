from flask import render_template, url_for, redirect, request

from .. import db
from . import auth
from .forms import AddProduct
from ..model import Product, Images


@auth.route('/register')
def register():
    return render_template('auth/register.html')


@auth.route('/login')
def login():
    return render_template('auth/login.html')


@auth.route('/logout')
def logout():
    return redirect(url_for('main.index'))


@auth.route('/account', methods=['POST', 'GET'])
def account():
    values = range(0, 5)
    add_product_form = AddProduct()

    if add_product_form.validate_on_submit():
        # TODO data input need to be made user safe
        name = add_product_form.name.data
        desc = add_product_form.description.data
        pic = request.files[add_product_form.image.name].read()
        cost = add_product_form.cost.data
        active = add_product_form.active.data

        item = Product(title=name,
                       description=desc,
                       cost=cost,
                       available=active,
                       stock_qty=10)
        db.session.add(item)
        item_id = item.proID

        query = db.session.query(db.func.count(Images.proID)).filter(Images.proID == item_id).scalar()

        return query

    return render_template('auth/account.html', list=values, add_product_form=add_product_form)

