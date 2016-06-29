from flask import url_for
from toollib.tool_lib import random_users
from app import create_app, db
import pytest


@pytest.fixture(scope='module')
def app(request):
    appx = create_app('testing')
    app_context = appx.app_context()
    app_context.push()
    client = appx.test_client(use_cookies=True)
    db.create_all()

    users = list(random_users())
    db.session.add_all(users)
    db.session.commit()

    def tearDown():
        db.session.remove()
        db.drop_all()
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


def test_register_passed(app):
    assert app.get(url_for('auth.registration_pass'))


def test_login(app):
    assert app.get(url_for('auth.login'))


def test_logout(app):
    assert app.get(url_for('auth.logout'))


def test_products_view(app):
    assert app.get(url_for('main.product_view', item='759325'))


def test_products_view_404(app):
    """
    Check the database, this error can be cased by no records in the data base
    """
    data = app.get(url_for('main.product_view', item='1'))
    assert 404 != data.status_code


def test_cart(app):
    assert app.get(url_for('main.cart'))


def test_account(app):
    assert app.get(url_for('auth.account'))


if __name__ == '__main__':

    pytest.main()
