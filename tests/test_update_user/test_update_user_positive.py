from main.user.helpers_user import HelpersCreateUser
from main.user.requests_user import RequestsCreateUser
from conftest import new_user_login


class TestUpdateUserPositive:
    def test_update_email(self, new_user_login):
        users_data = RequestsCreateUser.get_user(new_user_login.json()['accessToken'])

        new_email = HelpersCreateUser.generate_random_string(6) + '@test.ts'
        body = {
            'email': new_email,
            'name': users_data.json()['user']['name']
        }
        response = RequestsCreateUser.update_user(new_user_login.json()['accessToken'], body)

        assert response.status_code == 200 and response.json()['user']['email'] == new_email

    def test_update_name(self, new_user_login):
        users_data = RequestsCreateUser.get_user(new_user_login.json()['accessToken'])

        new_name = HelpersCreateUser.generate_random_string(10)
        body = {
            'email': users_data.json()['user']['email'],
            'name': new_name
        }
        response = RequestsCreateUser.update_user(new_user_login.json()['accessToken'], body)

        assert response.status_code == 200 and response.json()['user']['name'] == new_name
