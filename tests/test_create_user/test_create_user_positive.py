import allure

from main.user.helpers_user import HelpersUser
from main.user.requests_user import RequestsUser


class TestCreateUserPositive:
    @allure.title('Создание уникального пользователя')
    def test_create_user(self):
        credentials = HelpersUser.generate_credentials(email=True, password=True, name=True)
        response = RequestsUser.create_user(credentials)

        assert response.status_code == 200 and response.json()['user']['email'] == credentials['email']
