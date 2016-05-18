from flask import render_template, url_for, redirect
from . import auth


@auth.route('/register')
def register():
    return render_template('auth/register.html')


@auth.route('/login')
def login():
    return render_template('auth/login.html')


@auth.route('/logout')
def logout():
    return redirect(url_for('main.index'))


@auth.route('/account')
def account():
    values = range(0, 5)
    return render_template('auth/account.html', list=values)

