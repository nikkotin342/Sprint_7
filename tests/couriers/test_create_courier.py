import allure

from methods.courier_methods import CourierMethod
from tests import data



@allure.title('Проверка создания курьера с различными условиями')
class TestCreateCourier:

    def test_create_courier(self,create_courier_and_delete):
        response=create_courier_and_delete
        assert  response[0] == 201 and response[1] == data.COURIERS_201

    def test_create_courier_login_copy(self):
        response=CourierMethod().create_courier('qwerty1','12345','qwerty1')
        assert response[1] == data.COURIERS_409

    def test_create_courier_without_login(self):
        response=CourierMethod().create_without_login('12345','ytrewq')
        assert response[1] == data.COURIERS_400

    def test_create_courier_without_pass(self):
        response=CourierMethod().create_without_pass('12345','ytrewq')
        assert response[1] == data.COURIERS_400
