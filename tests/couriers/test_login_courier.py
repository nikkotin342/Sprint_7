import allure

from methods.courier_methods import CourierMethod
from tests import data


@allure.title('Проверка авторизации с различными условиями')
class TestLoginCourier:

    def test_login_courier(self):
        response = CourierMethod().login_courier('qwerty','qwerty')
        assert response[0] == 200 and 'id' in response[1]

    def test_login_courier_not_found(self):
        response = CourierMethod().login_courier('zzz','zzz')
        assert response[0] == 404

    def test_login_courier_wrong_login(self):
        response = CourierMethod().login_courier('data','qwerty')
        assert response[0] == 404

    def test_login_courier_wrong_pass(self):
        response = CourierMethod().login_courier('qwerty','data')
        assert response[0] == 404

    def test_login_courier_without_login(self):
        response = CourierMethod().login_without_login('qwerty')
        assert response[0] == 400 and response[1] == data.LOGIN_400
    def test_login_courier_without_pass(self):
        response = CourierMethod().login_without_pass('qwerty')
        assert response[0] == 400 and response[1] == data.LOGIN_400