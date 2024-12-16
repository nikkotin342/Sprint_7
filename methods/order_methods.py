import allure
import requests

from tests.data import BASE_URL, ORDERS_URL


class OrderMethods:

    @allure.step('Создание заказа')
    def post_order(self, name, surname, address, metro, phone, rent, date, comment, color):
        payload = {
    "firstName": name,
    "lastName": surname,
    "address": address,
    "metroStation": metro,
    "phone": phone,
    "rentTime": rent,
    "deliveryDate": date,
    "comment": comment,
    "color": color }
        response=requests.post(f'{BASE_URL}{ORDERS_URL}', json=payload)
        return response.status_code, response.json()

    @allure.step('Получить список заказов')
    def get_list_orders(self):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}')
        assert response.status_code, response.json()