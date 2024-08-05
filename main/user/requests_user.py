import requests

from data import *
from main.user.helpers_user import HelpersCreateUser


class RequestsCreateUser:
    @staticmethod
    def create_user(payload):
        response = requests.post(BASE_URL + CREATE_USER_PATH, data=payload)

        return response

    @staticmethod
    def login_user(payload):
        response = requests.post(BASE_URL + LOGIN_USER_PATH, data=payload)

        return response

    @staticmethod
    def update_user(access_token, payload):
        response = requests.patch(BASE_URL + AUTH_USER_PATH, headers={'Authorization': access_token}, data=payload)

        return response

    @staticmethod
    def update_user_without_token(payload):
        response = requests.patch(BASE_URL + AUTH_USER_PATH, data=payload)

        return response

    @staticmethod
    def get_user(access_token):
        response = requests.get(BASE_URL + AUTH_USER_PATH, headers={'Authorization': access_token})

        return response

    # @staticmethod
    # def create_user_and_get_credential():
    #     payload = HelpersCreateUser.generate_credentials(email=True, password=True, name=True)
    #
    #     response = RequestsCreateUser.user(payload)
    #
    #     if response.status_code == 200:
    #         return payload
    #
    #     return {}

    @staticmethod
    def delete_user(payload):
        response = requests.delete(BASE_URL + AUTH_USER_PATH, )