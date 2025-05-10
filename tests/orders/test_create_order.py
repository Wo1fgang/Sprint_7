import pytest
import allure
import data
from methods.order_methods import OrderMethod


class TestCreateOrder:

    @allure.title("тело ответа содержит track")
    def test_create_order(self):
        order = OrderMethod()
        status_code, text = order.create_order()
        assert status_code == 201 and "track" in text


    @allure.title('проверка цветов в заказе')
    @pytest.mark.parametrize("color_variant", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_colors_in_order(self, color_variant):

        data.order_data["color"] = color_variant
        order = OrderMethod()
        status_code, response_text = order.create_order()
        assert status_code == 201 and "track" in response_text

    @allure.title('проверка получения всех заказов')
    def test_get_all_orders(self):
        order = OrderMethod()
        status_code, response_text = order.get_all_orders()
        assert status_code == 200 and "orders" in response_text