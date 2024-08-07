import allure

from main.order.helpers_order import HelpersOrder
from main.order.requests_order import RequestsOrder
from conftest import new_user_login


class TestCreateOrderPositive:
    @allure.title('Создание заказа')
    def test_create_order(self, new_user_login):
        body = HelpersOrder.generate_body_with_ingredients()

        response = RequestsOrder.create_order(new_user_login.json()['accessToken'], body)

        assert (response.status_code == 200
                and 'owner' in response.json()['order']
                and '_id' in response.json()['order'])
