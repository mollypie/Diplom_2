import allure
import pytest

from main.user.helpers_user import HelpersUser
from main.user.requests_user import RequestsUser


class TestCreateUserNegative:
    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_exist_user(self):
        credentials = HelpersUser.generate_credentials(email=True, password=True, name=True)
        user_1 = RequestsUser.create_user(credentials)
        user_2 = RequestsUser.create_user(credentials)

        assert user_2.status_code == 403 and user_2.json()['message'] == 'User already exists'

        # delete user_1

    @allure.title('Создание пользователя без одного из обязательных полей')
    @pytest.mark.parametrize(
        'credentials',
        [
            [HelpersUser.generate_credentials(email=False, password=True, name=True)],
            [HelpersUser.generate_credentials(email=True, password=False, name=True)],
            [HelpersUser.generate_credentials(email=True, password=True, name=False)]
        ]
    )
    def test_create_user_without_required_fields(self, credentials):
        response = RequestsUser.create_user(credentials)

        assert response.status_code == 403 and response.json()['message'] == 'Email, password and name are required fields'
