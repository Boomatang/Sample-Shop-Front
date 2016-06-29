from app.model import User, Product
from forgery_py import internet, date, lorem_ipsum


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

if __name__ == '__main__':

    userlist = list(random_users())

    for user in userlist:
        print(user.email)
