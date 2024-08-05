import random
import string


class HelpersCreateUser:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def generate_credentials(email=False, password=False, name=False):
        credentials = {}

        if email:
            credentials['email'] = HelpersCreateUser.generate_random_string(6) + '@test.ts'

        if password:
            credentials['password'] = HelpersCreateUser.generate_random_string(10)

        if name:
            credentials['name'] = HelpersCreateUser.generate_random_string(10)

        return credentials

