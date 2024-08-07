import allure

from main.user.helpers_user import HelpersUser
from main.user.requests_user import RequestsUser


class TestUpdateUserNegative:
    @allure.title('Изменение email пользователя без авторизации')
    def test_update_email_negative(self):
        response = RequestsUser.update_user_without_token(HelpersUser.new_email())

        assert response.status_code == 401 and response.json()['message'] == 'You should be authorised'

    @allure.title('Изменение имени пользователя без авторизации')
    def test_update_name_negative(self):
        response = RequestsUser.update_user_without_token(HelpersUser.new_name())

        assert response.status_code == 401 and response.json()['message'] == 'You should be authorised'
