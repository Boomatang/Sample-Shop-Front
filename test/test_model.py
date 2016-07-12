from app.model import Product, Images, Owners, User


def test_product_create():
    prod = Product(proID=1, title='Test product')

    assert type(prod) == Product


def test_images_create():
    img = Images(imgID=1, name='test_img.jpg')

    assert type(img) == Images


def test_owners_create():
    owner = Owners(name='John')

    assert type(owner) == Owners


def test_user_create():
    user = User(id=1, username='TIMTIM')

    assert type(user) == User


def test_user_password_read():
    user = User(id=1, username='TIMTIM')

    try:
        user.password
        assert False
    except AttributeError:
        assert True


def test_password_hash():
    user = User(id=1, username='TIMTIM')
    word = "haircut"

    user.password = word

    assert user.verify_password(word)
