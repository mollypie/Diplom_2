import pytest

from main.user.helpers_user import HelpersCreateUser
from main.user.requests_user import RequestsCreateUser


@pytest.fixture(scope='class')
def new_user_create():
    credentials = HelpersCreateUser.generate_credentials(email=True, password=True, name=True)
    RequestsCreateUser.create_user(credentials)

    yield {
        'email': credentials['email'],
        'password': credentials['password']
    }

    # RequestsCreateUser.delete_courier(new_user)


@pytest.fixture(scope='class')
def new_user_login():
    credentials = HelpersCreateUser.generate_credentials(email=True, password=True, name=True)
    RequestsCreateUser.create_user(credentials)

    credentials_for_login = {
        'email': credentials['email'],
        'password': credentials['password']
    }
    new_user = RequestsCreateUser.login_user(credentials_for_login)

    yield new_user

    # RequestsCreateUser.delete_courier(new_user)
