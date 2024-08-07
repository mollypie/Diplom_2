import allure

from main.order.helpers_order import HelpersOrder
from main.order.requests_order import RequestsOrder
from conftest import new_user_login
from main.user.helpers_user import HelpersUser


class TestGetOrdersPositive:
    @allure.title('Получение заказов авторизованного пользователя')
    def test_get_orders(self, new_user_login):
        body = HelpersOrder.generate_body_with_ingredients()
        RequestsOrder.create_order(HelpersUser.get_token(new_user_login), body)

        response = RequestsOrder.get_orders(HelpersUser.get_token(new_user_login))

        assert response.status_code == 200 and len(response.json()['orders']) > 0
