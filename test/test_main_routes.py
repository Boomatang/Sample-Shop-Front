from flask import url_for
from app import create_app, db
import pytest



@pytest.fixture(scope='module')
def app(request):

    appx = create_app('testing')
    app_context = appx.app_context()
    app_context.push()
    client = appx.test_client(use_cookies=True)
    db.create_all()

    def tearDown():
        app_context.pop()
    request.addfinalizer(tearDown)
    return client


def test_index(app):
    assert app.get(url_for('main.index'))


def test_testing(app):
    assert app.get(url_for('testing.testing'))


def test_products(app):
    assert app.get(url_for('main.products'))


def test_contact_us(app):
    assert app.get(url_for('main.contact'))


def test_register(app):
    assert app.get(url_for('auth.register'))


def test_login(app):
    assert app.get(url_for('auth.login'))


def test_logout(app):
    assert app.get(url_for('auth.logout'))


def test_products_view(app):
    assert app.get(url_for('main.product_view', item='759325'))


def test_cart(app):
    assert app.get(url_for('main.cart'))


def test_account(app):
    assert app.get(url_for('auth.account'))

