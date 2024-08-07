import requests

from data import *


class RequestsOrder:
    @staticmethod
    def create_order(access_token, payload):
        response = requests.post(BASE_URL + ORDER, headers={'Authorization': access_token}, data=payload)

        return response

    @staticmethod
    def create_order_without_token(payload):
        response = requests.post(BASE_URL + ORDER, data=payload)

        return response

    @staticmethod
    def get_ingredients():
        response = requests.get(BASE_URL + GET_INGREDIENTS)

        return response

    @staticmethod
    def get_orders(access_token):
        response = requests.get(BASE_URL + ORDER, headers={'Authorization': access_token})

        return response

    @staticmethod
    def get_orders_without_token():
        response = requests.get(BASE_URL + ORDER)

        return response
