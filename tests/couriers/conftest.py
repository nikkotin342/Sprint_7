import random
import time


import pytest

from methods.courier_methods import CourierMethod


@pytest.fixture()
def courier_data():
    return {f"makki_{random.randint(100, 9999)}",f"makki_{random.randint(100, 9999)}",f"makki_{random.randint(100, 9999)}"}


@pytest.fixture()
def create_courier_and_delete(courier_data):
    response=CourierMethod().create_courier(*courier_data)
    response_lp = CourierMethod().login_courier(*response[2])
    response_del = CourierMethod().delete_courier(response_lp[1]['id'])
    return response[0], response[1]



