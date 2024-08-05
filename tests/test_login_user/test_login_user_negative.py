from main.user.helpers_user import HelpersCreateUser
from main.user.requests_user import RequestsCreateUser
from conftest import new_user_create


class TestLoginUserNegative:
    def test_login_user_with_invalid_credentials(self, new_user_create):
        user = new_user_create
        invalid_credentials = HelpersCreateUser.generate_credentials(email=True, password=True, name=False)
        response = RequestsCreateUser.login_user(invalid_credentials)

        assert response.status_code == 401 and response.json()['message'] == 'email or password are incorrect'
