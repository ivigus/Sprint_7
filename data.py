import random
import string
class AcceptOrder:
    Url_accept_order_1 =     'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/145?courierId=585596'
    Url_accept_order_2 =     'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/386594?courierId=123'
    Url_accept_order_3 =     'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/1149?courierId=12'
    Url_accept_order_4 =     'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/386594?courierId'
    Url_accept_order_5 =     'https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t=343249'
    create_an_order_1 =      'https://qa-scooter.praktikum-services.ru/api/v1/orders'
    can_be_created_courier = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
    order_not_found_1 =      'https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t=1'
    order_not_found_2 =      'https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t='
    order_not_found_3 =      'https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t=343249'
    list_of_orders =         'https://qa-scooter.praktikum-services.ru/api/v1/orders?courierId=585593'
    remove_courier_1 =       'https://qa-scooter.praktikum-services.ru/api/v1/courier/1'
    remove_courier_2 =       'https://qa-scooter.praktikum-services.ru/api/v1/courier/'
    remove_courier_3 =       'https://qa-scooter.praktikum-services.ru/api/v1/courier/585595'
    сourier_login =          'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'

class TextOfMistake:
    errer_1 = 'Заказа с таким id не существует'
    errer_2 = 'Курьера с таким id не существует'
    errer_3 = 'Недостаточно данных для поиска'
    errer_4 = 'Недостаточно данных для создания учетной записи'
    errer_5 = "Заказ не найден"
    errer_6 = 'Учетная запись не найдена'

class DataForTheTest:
    payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK", "GREY"]
    }
    payload_1 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }
    payload_2 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["GREY"]
    }
    payload_3 = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha"
    }

class CreateDataForUse:
    @staticmethod
    def generate_random_string(length):
        """Генерация случайной строки"""
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def register_new_courier():
        login = CreateDataForUse.generate_random_string(10)
        password = CreateDataForUse.generate_random_string(10)
        first_name = CreateDataForUse.generate_random_string(10)

        payload = {
        "login": login,
        "password": password,
        "first_name": first_name
        }
        return payload