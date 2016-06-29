import os


def test_mail_username():
    assert os.environ.get('MAIL_USERNAME') is not None


def test_mail_password():
    assert os.environ.get('MAIL_PASSWORD') is not None


def test_secret_key():

    assert os.environ.get('SECRET_KEY') is not None


def test_site_admin():
    assert os.environ.get('SITE_ADMIN') is not None



