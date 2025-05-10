import requests

import data
import helpers

from data import BASE_URL, COURIER, LOGIN


class CourierMethods:

    def register_new_courier_and_return_login_password(self, params = None):
        self.params = params
        login_pass = []
        login = helpers.generate_random_string(20)
        password = helpers.generate_random_string(20)
        first_name = helpers.generate_random_string(20)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        if self.params == "create_new":
            response = requests.post(f'{BASE_URL}{COURIER}', data=payload)
        elif self.params == "create_exciting":
            response = requests.post(f'{BASE_URL}{COURIER}', data=data.payload)
        elif self.params == "create_invalid_courier":
            response = requests.post(f'{BASE_URL}{COURIER}', data=data.invalid_payload)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        return response.status_code, response.text, login_pass


    def login_courier(self, params):
        self.params = params

        if self.params == "login":
            response = requests.post(f'{BASE_URL}{COURIER}{LOGIN}', data = data.payload)
        elif self.params == "invalid_login":
            response = requests.post(f'{BASE_URL}{COURIER}{LOGIN}', data = data.invalid_payload)
        elif self.params == "incorrect_login":
            response = requests.post(f'{BASE_URL}{COURIER}{LOGIN}', data = data.incorrect_payload)

        return response.status_code, response.text
