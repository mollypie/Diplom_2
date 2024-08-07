import allure

from data import *
from main.order.requests_order import RequestsOrder


class TestGetOrdersNegative:
    @allure.title('Получение заказов неавторизованного пользователя')
    def test_get_orders_without_token(self):
        response = RequestsOrder.get_orders_without_token()

        assert response.status_code == 401 and response.json()['message'] == TEXT_USER_UNAUTHORISED
