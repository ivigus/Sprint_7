import allure
import requests
import pytest
from data import AcceptOrder, TextOfMistake, CreateDataForUse

class TestCourierRegistration:

    @pytest.fixture(autouse=True)
    def setup_courier_data(self):
        """Фикстура для подготовки данных курьера"""
        self.payload = CreateDataForUse.register_new_courier()
        yield

    @allure.title('Успешная регистрация курьера и получение ID при логине')
    def test_successful_request_returns_id(self):
        response = requests.post(AcceptOrder.can_be_created_courier, data=self.payload)
        assert response.status_code == 201

        auth_payload = {"login": self.payload["login"], "password": self.payload["password"]}
        response = requests.post(AcceptOrder.сourier_login, data=auth_payload)
        assert 'id' in response.json()


class TestCourierLogin:

    @pytest.fixture(autouse=True)
    def setup_and_register_courier(self):
        self.payload = CreateDataForUse.register_new_courier()
        requests.post(AcceptOrder.can_be_created_courier, data=self.payload)
        yield

    @allure.title('Успешный логин зарегистрированного курьера')
    def test_courier_can_log_in(self):
        auth_payload = {"login": self.payload["login"], "password": self.payload["password"]}
        response = requests.post(AcceptOrder.сourier_login, data=auth_payload)
        assert response.status_code == 200

    @allure.title('Ошибка при логине несуществующего курьера')
    def test_non_existent_user(self):
        auth_payload = {"login": "nonexistent", "password": "password123"}
        response = requests.post(AcceptOrder.сourier_login, data=auth_payload)
        assert response.json()['message'] == TextOfMistake.error_6

    @allure.title('Ошибка при логине без указания логина')
    def test_missing_login_field(self):
        auth_payload = {"password": self.payload["password"]}
        response = requests.post(AcceptOrder.сourier_login, data=auth_payload)
        assert response.json()['code'] == 400