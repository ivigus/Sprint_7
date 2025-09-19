import requests
import random
import string
from Sprint_7.data import AcceptOrder,TextOfMistake,CreateDataForUse


class TestCourierRegistration:
    """Тесты регистрации курьера"""

    def test_register_new_courier_and_return_login_password(self):
        """Регистрация нового курьера и возврат данных"""
        login_pass = []
        payload = CreateDataForUse.register_new_courier()
        response = requests.post(AcceptOrder.can_be_created_courier, data=payload)
        if response.status_code == 201:
            login_pass.extend([payload["login"], payload["password"], payload["first_name"]])
        print(login_pass)
        return login_pass

    def test_successful_request_returns_valid_data(self):
        """Успешная регистрация возвращает корректные данные"""
        payload = CreateDataForUse.register_new_courier()
        response = requests.post(AcceptOrder.can_be_created_courier, data=payload)
        assert response.json() == {'ok': True}

    def test_all_required_fields_no_login(self):
        """Проверка обязательности поля login"""
        payload = CreateDataForUse.register_new_courier()
        del payload["login"]

        response = requests.post(AcceptOrder.can_be_created_courier, data=payload)
        assert response.json()['message'] == TextOfMistake.errer_4

    def test_all_required_fields_no_pass(self):
        """Проверка обязательности поля password"""
        payload = CreateDataForUse.register_new_courier()
        del payload["password"]  # Удаляем поле password

        response = requests.post(AcceptOrder.can_be_created_courier, data=payload)
        assert response.json()['message'] == TextOfMistake.errer_4

    def test_register_new_courier_status_code(self):
        """Проверка кода ответа при регистрации"""
        payload = CreateDataForUse.register_new_courier()
        response = requests.post(AcceptOrder.can_be_created_courier, data=payload)
        assert response.status_code == 201

    def test_cannot_create_identical_couriers(self):
        """Проверка создания дубликатов курьеров"""
        login = 'sanek51'
        password = '12345'
        first_name = 'sanek15'

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # Первый запрос - создаем курьера
        response1 = requests.post(AcceptOrder.can_be_created_courier, data=payload)

        # Второй запрос - пытаемся создать такого же
        response2 = requests.post(AcceptOrder.can_be_created_courier, data=payload)
        assert response2.status_code == 409

