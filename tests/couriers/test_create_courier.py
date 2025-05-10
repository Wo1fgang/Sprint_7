import allure
from methods.courier_methods import CourierMethods


class TestCourier:

    @allure.title('курьера можно создать / успешный запрос возвращает "ok":true / запрос возвращает правильный код ответа')
    def test_create_courier(self):
        new_courier = CourierMethods()
        status_code, text, _ = new_courier.register_new_courier_and_return_login_password("create_new")
        assert status_code == 201 and text == '{"ok":true}'

    @allure.title('нельзя создать двух одинаковых курьеров / если создать пользователя с логином, который уже есть, возвращается ошибка')
    def test_create_existing_courier(self):
        new_courier = CourierMethods()
        status_code, text, _ = new_courier.register_new_courier_and_return_login_password("create_exciting")
        assert status_code == 409 and text == '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'

    @allure.title('чтобы создать курьера, нужно передать в ручку все обязательные поля / если одного из полей нет, запрос возвращает ошибку')
    def test_create_existing_courier(self):
        new_courier = CourierMethods()
        status_code, text, _ = new_courier.register_new_courier_and_return_login_password("create_invalid_courier")
        assert status_code == 400 and text == '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
