import allure

from methods.order_methods import OrderMethods

@allure.title('Проверка получения списка заказов')
class TestGetListOrders:
    def test_get_list_orders(self):
        response = OrderMethods().get_list_orders()
        assert response[0] == 200