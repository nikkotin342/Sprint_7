import allure

from methods.courier_methods import CourierMethod


@allure.title('Проверка создания курьера с различными условиями')
class TestCreateCourier:

    def test_create_courier(self,courier_data):
        response=CourierMethod().create_courier(*courier_data)
        assert response[0] == 201 and response[1] == {"ok": True}

    def test_create_courier_login_copy(self):
        response=CourierMethod().create_courier('qwerty1','12345','qwerty1')
        assert response[1] == {'code': 409, "message": 'Этот логин уже используется. Попробуйте другой.'}

    def test_create_courier_without_login(self):
        response=CourierMethod().create_without_login('12345','ytrewq')
        assert response[1] == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}

    def test_create_courier_without_pass(self):
        response=CourierMethod().create_without_pass('12345','ytrewq')
        assert response[1] == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
