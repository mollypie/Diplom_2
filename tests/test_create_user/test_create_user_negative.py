import allure
import pytest

from main.user.helpers_user import HelpersCreateUser
from main.user.requests_user import RequestsCreateUser


class TestCreateUserNegative:
    @allure.title('Создание двух одинаковых пользователей')
    def test_create_exist_user(self):
        credentials = HelpersCreateUser.generate_credentials(email=True, password=True, name=True)
        user_1 = RequestsCreateUser.create_user(credentials)
        user_2 = RequestsCreateUser.create_user(credentials)

        assert user_2.status_code == 403 and user_2.json()['message'] == 'User already exists'

        # delete user_1

    @allure.title('Создание пользователя без одного из обязательных полей')
    @pytest.mark.parametrize(
        'credentials',
        [
            [HelpersCreateUser.generate_credentials(email=False, password=True, name=True)],
            [HelpersCreateUser.generate_credentials(email=True, password=False, name=True)],
            [HelpersCreateUser.generate_credentials(email=True, password=True, name=False)]
        ]
    )
    def test_create_user_without_required_fields(self, credentials):
        response = RequestsCreateUser.create_user(credentials)

        assert response.status_code == 403 and response.json()['message'] == 'Email, password and name are required fields'
