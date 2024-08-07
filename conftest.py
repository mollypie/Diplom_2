import pytest

from main.user.helpers_user import HelpersUser
from main.user.requests_user import RequestsUser


@pytest.fixture(scope='class')
def new_user_create():
    credentials = HelpersUser.generate_credentials(email=True, password=True, name=True)
    RequestsUser.create_user(credentials)

    yield {
        'email': credentials['email'],
        'password': credentials['password']
    }

    credentials_for_login = HelpersUser.credentials_for_login(credentials)

    new_user = RequestsUser.login_user(credentials_for_login)

    RequestsUser.delete_user(new_user.json()['accessToken'])


@pytest.fixture(scope='class')
def new_user_login():
    credentials = HelpersUser.generate_credentials(email=True, password=True, name=True)
    RequestsUser.create_user(credentials)

    credentials_for_login = HelpersUser.credentials_for_login(credentials)

    new_user = RequestsUser.login_user(credentials_for_login)

    yield new_user

    RequestsUser.delete_user(new_user.json()['accessToken'])
