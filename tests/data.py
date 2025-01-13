

BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
ORDERS_URL = 'orders/'
COURIERS_URL = 'courier/'

ORDER_DATA_1= ['qwerty', 'qwerty', 'qwerty', 'qwerty', 'qwerty', 5, '2024-12-12', 'qwerty', ['BLACK']]
ORDER_DATA_2= ['qwerty1', 'qwerty1', 'qwerty1', 'qwerty1', 'qwerty1', 5, '2024-12-13', 'qwerty1', ['GREY']]
ORDER_DATA_3= ['qwerty2', 'qwerty2', 'qwerty2', 'qwerty2', 'qwerty2',5 , '2024-12-14', 'qwerty2', ['GREY','BLACK']]
ORDER_DATA_4=['qwerty2', 'qwerty2', 'qwerty2', 'qwerty2', 'qwerty2', 5, '2024-12-14', 'qwerty2', []]

COURIERS_400={'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
COURIERS_409={'code': 409, "message": 'Этот логин уже используется. Попробуйте другой.'}
COURIERS_201={"ok": True}
LOGIN_400={'code': 400, 'message': 'Недостаточно данных для входа'}