import allure

from main.user.helpers_user import HelpersUser
from main.user.requests_user import RequestsUser
from conftest import new_user_login


class TestUpdateUserPositive:
    @allure.title('Изменение email пользователя')
    def test_update_email(self, new_user_login):
        users_data = RequestsUser.get_user(new_user_login.json()['accessToken'])
        new_email = HelpersUser.new_email()

        response = RequestsUser.update_user(new_user_login.json()['accessToken'], new_email)

        assert (response.status_code == 200
                and response.json()['user']['email'] == new_email['email']
                and response.json()['user']['name'] == users_data.json()['user']['name'])

    @allure.title('Изменение имени пользователя')
    def test_update_name(self, new_user_login):
        users_data = RequestsUser.get_user(new_user_login.json()['accessToken'])
        new_name = HelpersUser.new_name()

        response = RequestsUser.update_user(new_user_login.json()['accessToken'], new_name)

        assert (response.status_code == 200
                and response.json()['user']['name'] == new_name['name']
                and response.json()['user']['email'] == users_data.json()['user']['email'])
