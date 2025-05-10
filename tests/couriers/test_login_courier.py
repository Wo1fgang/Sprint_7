import allure
from methods.courier_methods import CourierMethods


class TestLoginCourier:

    @allure.title('курьер может авторизоваться / успешный запрос возвращает id')
    def test_login_courier(self):
        courier = CourierMethods()
        status_code, text = courier.login_courier("login")
        assert status_code == 200 and text == '{"id":513941}'

    @allure.title(
        'для авторизации нужно передать все обязательные поля / если какого-то поля нет, запрос возвращает ошибку')
    def test_login_with_invalid_data(self):
        courier = CourierMethods()
        status_code, text = courier.login_courier("invalid_login")
        assert status_code == 400 and text == '{"code":400,"message":"Недостаточно данных для входа"}'

    @allure.title(
        'система вернёт ошибку, если неправильно указать логин или пароль / если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    def test_login_with_incorrect_password(self):
        courier = CourierMethods()
        status_code, text = courier.login_courier("incorrect_login")
        assert status_code == 404 and text == '{"code":404,"message":"Учетная запись не найдена"}'
