import random
import string


class HelpersUser:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def generate_credentials(email=False, password=False, name=False):
        credentials = {}

        if email:
            credentials['email'] = HelpersUser.generate_random_email(6)

        if password:
            credentials['password'] = HelpersUser.generate_random_string(10)

        if name:
            credentials['name'] = HelpersUser.generate_random_string(10)

        return credentials

    @staticmethod
    def generate_random_email(num_email):
        email = HelpersUser.generate_random_string(num_email) + '@test.ts'

        return email

    @staticmethod
    def new_email():
        new_email = HelpersUser.generate_random_email(6)

        body_with_new_email = {
            'email': new_email
        }

        return body_with_new_email

    @staticmethod
    def new_name():
        new_name = HelpersUser.generate_random_string(9)

        body_with_new_name = {
            'name': new_name
        }

        return body_with_new_name
