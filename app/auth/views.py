import os
from flask import render_template, url_for, redirect, request
from sqlalchemy import func

from .. import db
from . import auth
from .forms import AddProduct
from ..model import Product, Images
from werkzeug import secure_filename
from ..functions import get_all, UPLOADS_PHOTO_DIR


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
        pic = request.files[add_product_form.image.name]
        pic_name = secure_filename(pic.filename)
        pic_name = pic_name.split('.')

        ext = pic_name[1]

        cost = add_product_form.cost.data
        active = add_product_form.active.data

        proId = db.session.query(func.max(Product.proID)).scalar()

        if proId:
            proId += 1
        else:
            proId = 1
        item = Product(proID=proId,
                       title=name,
                       description=desc,
                       cost=cost,
                       available=active,
                       stock_qty=10)
        db.session.add(item)
        db.session.commit()

        uploaded = db.session.query(Product).filter(Product.proID == proId).one()

        img_id = db.session.query(db.func.count(Images.imgID)).filter(Images.proID == uploaded.proID).scalar()
        img_id_all = db.session.query(db.func.count(Images.imgID)).scalar()
        img_name = 'P' + str(uploaded.proID) + '-I' + str(img_id) + '.' + ext

        pic.save(os.path.join(UPLOADS_PHOTO_DIR, img_name))

        if img_id_all:
            img_id_all += 1
        else:
            img_id_all = 1

        image_item = Images(imgID=img_id_all, name=img_name, proID=uploaded.proID)
        if not uploaded.default_image_ID:
            uploaded.default_image_ID = img_id_all
        db.session.add_all([image_item, uploaded])
        db.session.commit()
        get_all(UPLOADS_PHOTO_DIR)

        return img_name

    return render_template('auth/account.html',
                           list=values,
                           add_product_form=add_product_form)

