BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
COURIER = 'courier/'
LOGIN = 'login'
ORDERS = 'orders/'

payload = {
    "login": "wolfgang",
    "password": "1234"
}

invalid_payload = {
    "login": "wolfgang",
    "password": ""
}

incorrect_payload = {
    "login": "wolfgang",
    "password": "123"
}

order_data = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": "4",
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
    ]
}