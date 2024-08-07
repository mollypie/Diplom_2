import random

from main.order.requests_order import RequestsOrder
from main.user.helpers_user import HelpersUser


class HelpersOrder:
    @staticmethod
    def generate_ingredients():
        list_ingredients = []

        ingredients = RequestsOrder.get_ingredients()

        for ingredient in ingredients.json()['data']:
            list_ingredients.append(ingredient['_id'])

        random_ingredients = random.choices(list_ingredients, k=3)

        return random_ingredients

    @staticmethod
    def generate_invalid_ingredients():
        list_ingredients = ['60' + HelpersUser.generate_random_string(18) + '33c6']

        return list_ingredients

    @staticmethod
    def generate_body_with_ingredients():
        ingredients = HelpersOrder.generate_ingredients()
        body_with_random_ingredients = {"ingredients": ingredients}

        return body_with_random_ingredients

    @staticmethod
    def generate_body_with_invalid_ingredients():
        ingredients = HelpersOrder.generate_invalid_ingredients()
        body_with_random_ingredients = {"ingredients": ingredients}

        return body_with_random_ingredients

    @staticmethod
    def generate_body_without_ingredients():
        body_without_ingredients = {"ingredients": []}

        return body_without_ingredients
