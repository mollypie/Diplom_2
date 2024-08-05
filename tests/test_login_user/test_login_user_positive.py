from main.user.requests_user import RequestsCreateUser
from conftest import new_user_create


class TestLoginUserPositive:
    def test_login_user(self, new_user_create):
        response = RequestsCreateUser.login_user(new_user_create)

        assert (response.status_code == 200
                and 'accessToken' in response.text
                and 'refreshToken' in response.text)
