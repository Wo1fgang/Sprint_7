import requests
import data

from data import BASE_URL, ORDERS


class  OrderMethod:

    def create_order(self):
        response = requests.post(f'{BASE_URL}{ORDERS}', json=data.order_data)
        return response.status_code, response.text

    def get_all_orders(self):
        response = requests.get(f'{BASE_URL}{ORDERS}')
        return response.status_code, response.text