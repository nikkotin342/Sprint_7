import requests
import allure

from tests.data import BASE_URL, COURIERS_URL


class CourierMethod:

    @allure.step('Создать курьера')
    def create_courier(self, login, password, first_name):
        payload = {"login": login,
        "password": password,
        "firstName": first_name}
        respone=requests.post(f'{BASE_URL}{COURIERS_URL}',data=payload)
        return respone.status_code,respone.json()

    @allure.step('Создать курьера без логина')
    def create_without_login(self, password, first_name):
        payload = {"password": password,
                   "firstName": first_name}
        respone = requests.post(f'{BASE_URL}{COURIERS_URL}', data=payload)
        return respone.status_code, respone.json()

    @allure.step('Создать курьера без пароля')
    def create_without_pass(self, login, first_name):
        payload = {"login": login,
                   "firstName": first_name}
        respone = requests.post(f'{BASE_URL}{COURIERS_URL}', data=payload)
        return respone.status_code, respone.json()

    @allure.step('Авторизация курьера')
    def login_courier(self, login, password):
        payload = {"login": login,'password': password}
        respone = requests.post(f'{BASE_URL}{COURIERS_URL}login', data=payload)
        return respone.status_code, respone.json()

    @allure.step('Авторизация курьера без логина')
    def login_without_login(self, password):
        payload = {"password": password}
        respone = requests.post(f'{BASE_URL}{COURIERS_URL}login', data=payload)
        return respone.status_code, respone.json()

    @allure.step('Авторизация курьера без пароля')
    def login_without_pass(self, login):
        payload = {"login": login}
        response = requests.post(f'{BASE_URL}{COURIERS_URL}login', data=payload)
        return response.status_code, response.json()



