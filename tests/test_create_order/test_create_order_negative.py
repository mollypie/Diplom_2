import allure

from data import *
from main.order.helpers_order import HelpersOrder
from main.order.requests_order import RequestsOrder
from conftest import new_user_login
from main.user.helpers_user import HelpersUser


class TestCreateOrderNegative:
    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self, new_user_login):
        body = HelpersOrder.generate_body_without_ingredients()

        response = RequestsOrder.create_order(HelpersUser.get_token(new_user_login), body)

        assert response.status_code == 400 and response.json()['message'] == TEXT_ORDER_WITHOUT_INGREDIENT

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_token(self):
        body = HelpersOrder.generate_body_with_ingredients()

        response = RequestsOrder.create_order_without_token(body)

        assert (response.status_code == 200
                and 'owner' not in response.json()['order']
                and 'number' in response.json()['order'])

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_with_invalid_ingredients(self, new_user_login):
        body = HelpersOrder.generate_body_with_invalid_ingredients()

        response = RequestsOrder.create_order(HelpersUser.get_token(new_user_login), body)

        assert response.status_code == 500
