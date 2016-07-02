from datetime import datetime
from os import path
from pathlib import Path as P

from app import db
from app.model import User, Product, Images
from forgery_py import internet, date, lorem_ipsum
from app.functions import ext_allowed, IMAGE_SAVE_PATH, get_products, get_all, UPLOADS_PHOTO_DIR, setup_img
from random import randint
import shutil

__all__ = ['random_products', 'random_users', 'add_default_images']


def create_random_product():
    title = lorem_ipsum.words(randint(1, 5))
    description = lorem_ipsum.paragraphs(randint(1, 3), html=True)
    cost = randint(1.00, 100.00)
    available = True
    stock_qty = randint(1, 20)

    return Product(title=title, description=description, cost=cost, available=available, stock_qty=stock_qty)


def random_products(qty=20):
    x = 0
    while x < qty:
        yield create_random_product()
        x += 1


def create_random_user():
    username = internet.user_name()
    email = internet.email_address()
    signup_date = date.date(past=True)
    password = lorem_ipsum.word()

    return User(username=username, email=email, signup_date=signup_date, password=password)


def random_users(qty=50):
    x = 0
    while x < qty:
        yield create_random_user()
        x += 1


def random_image_list():
    output = []
    img_dir = '/home/boomatang/Projects/Web_sites/Sample-Shop-Front/sample_pics'
    basedir = path.abspath(path.dirname(__file__))
    # folder = P(path.join(basedir, 'sample_pics'))
    folder = P(img_dir)

    contents = folder.iterdir()

    for content in contents:
        try:
            if ext_allowed(content.name):
                output.append(path.join(img_dir,content.name))
        except IndexError:
            pass
    return output


def copy_images(img_path):
    copy_to = IMAGE_SAVE_PATH

    print(copy_to)


def add_default_images():
    # get list of products.
    hard_path = '/home/boomatang/Projects/Web_sites/Sample-Shop-Front/app/static/uploads'
    values = get_products(limit=-1)
    img_list = random_image_list()
    for value in values:
        # get image
        list_count = len(img_list)
        img_id = randint(1, list_count) - 1
        img = img_list[img_id]
        img_list.pop(img_id)

        pic_name = img.split('.')
        ext = pic_name[1]

       # uploaded = db.session.query(Product).filter(Product.proID == proId).one()

        img_id = db.session.query(db.func.count(Images.imgID)).filter(Images.proID == value.proID).scalar()
        img_id_all = db.session.query(db.func.count(Images.imgID)).scalar()
        img_name = 'P' + str(value.proID) + '-I' + str(img_id) + '.' + ext

        if img_id_all:
            img_id_all += 1
        else:
            img_id_all = 1

        image_item = Images(imgID=img_id_all, name=img_name, proID=value.proID)
        if not value.default_image_ID:
            value.default_image_ID = img_id_all
        db.session.add_all([image_item, value])
        db.session.commit()

        shutil.copy(img, path.join(hard_path, img_name))



    get_all(UPLOADS_PHOTO_DIR)

    # get the image name
    # set the image to be the default
    # upload the image using the new name
    # run the resize function




if __name__ == '__main__':
    start = datetime.now()

    images = random_image_list()
    add_default_images()
    print(datetime.now() - start)
    for i in images:
        print(i)
    print(len(images))
