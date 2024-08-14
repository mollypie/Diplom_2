import requests

from data import *


class RequestsUser:
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

    @staticmethod
    def delete_user(access_token):
        response = requests.delete(BASE_URL + AUTH_USER_PATH, headers={'Authorization': access_token})

        return response
