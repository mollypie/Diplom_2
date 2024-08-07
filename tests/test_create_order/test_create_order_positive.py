import allure

from main.order.helpers_order import HelpersOrder
from main.order.requests_order import RequestsOrder
from conftest import new_user_login
from main.user.helpers_user import HelpersUser


class TestCreateOrderPositive:
    @allure.title('Создание заказа')
    def test_create_order(self, new_user_login):
        body = HelpersOrder.generate_body_with_ingredients()

        response = RequestsOrder.create_order(HelpersUser.get_token(new_user_login), body)

        assert (response.status_code == 200
                and 'owner' in response.json()['order']
                and '_id' in response.json()['order'])
