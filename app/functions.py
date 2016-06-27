import os
from PIL import Image
from pathlib import Path as P


from . import db
from .model import Images

folder_list = ['150x200', '171x180', '200x240', '250x300', '319x200', '75x90']
UPLOADS_PHOTO = 'static/uploads'

baseDir = os.path.abspath(os.path.dirname(__file__))

UPLOADS_PHOTO_DIR = os.path.join(baseDir, UPLOADS_PHOTO)
IMAGE_SAVE_PATH = os.path.join(baseDir, 'static/images')


def image_resize(img, size):
    size = size.split('x')
    width = size[0]
    height = size[1]
    size = (int(width), int(height))

    output = img.resize(size)

    return output


def image_type(img_path):
    img = Image.open(img_path)

    output = img.copy()
    img.close()
    return output


def setup_img(image, save):

    img_odj = P(image)

    for location in folder_list:
        i = image_type(image)

        i_new = image_resize(i, location)

        i_new.save(os.path.join(save, location, img_odj.name))

        i.close()
        i_new.close()

    img_odj.unlink()


def ext_allowed(check):
    allowed = ['jpg', 'png']
    show = check.split('.')
    if show[1].lower() in allowed:
        return True
    else:
        return False


def get_all(start_point):
    start = P(start_point)

    contents = start.iterdir()

    for ifile in contents:
        if ifile.is_file() and ext_allowed(ifile.name):
            setup_img(ifile, IMAGE_SAVE_PATH)


def get_default_image(img_id):
    query = db.session.query(Images).filter(Images.imgID == img_id).one()
    return query.name


if __name__ == '__main__':

    pass
