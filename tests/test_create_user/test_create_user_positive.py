from main.user.helpers_user import HelpersCreateUser
from main.user.requests_user import RequestsCreateUser


class TestCreateUserPositive:
    def test_create_user(self):
        credentials = HelpersCreateUser.generate_credentials(email=True, password=True, name=True)
        response = RequestsCreateUser.create_user(credentials)

        assert response.status_code == 200 and response.json()['user']['email'] == credentials['email']
