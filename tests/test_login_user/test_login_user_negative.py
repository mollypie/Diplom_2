import allure

from data import *
from main.user.helpers_user import HelpersUser
from main.user.requests_user import RequestsUser
from conftest import new_user_create


class TestLoginUserNegative:
    @allure.title('Логин с неверным паролем')
    def test_login_user_with_invalid_password(self, new_user_create):
        invalid_credentials = {
            'email': new_user_create['email'],
            'password': HelpersUser.generate_random_string(9)
        }

        response = RequestsUser.login_user(invalid_credentials)

        assert response.status_code == 401 and response.json()['message'] == TEXT_EMAIL_OR_PASSWORD_INCORRECT

    @allure.title('Логин с неверным логином')
    def test_login_user_with_invalid_email(self, new_user_create):
        invalid_credentials = {
            'email': HelpersUser.generate_random_email(7),
            'password': new_user_create['password']
        }

        response = RequestsUser.login_user(invalid_credentials)

        assert response.status_code == 401 and response.json()['message'] == TEXT_EMAIL_OR_PASSWORD_INCORRECT
