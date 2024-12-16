import allure
import pytest


from methods.order_methods import OrderMethods
from tests import data



@allure.title('Проверка создания заказа с различными условиями')
class TestCreateOrder:
    @pytest.mark.parametrize('data',[data.ORDER_DATA_1, data.ORDER_DATA_2,data.ORDER_DATA_3,data.ORDER_DATA_4])
    def test_create_order(self,data):
        response = OrderMethods().post_order(*data)
        assert response[0] == 201 and 'track' in response[1]
