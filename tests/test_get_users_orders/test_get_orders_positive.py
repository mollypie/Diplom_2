import allure

from main.order.helpers_order import HelpersOrder
from main.order.requests_order import RequestsOrder
from conftest import new_user_login


class TestGetOrdersPositive:
    @allure.title('Получение заказов авторизованного пользователя')
    def test_get_orders(self, new_user_login):
        body = HelpersOrder.generate_body_with_ingredients()
        RequestsOrder.create_order(new_user_login.json()['accessToken'], body)

        response = RequestsOrder.get_orders(new_user_login.json()['accessToken'])

        assert response.status_code == 200 and len(response.json()['orders']) > 0
