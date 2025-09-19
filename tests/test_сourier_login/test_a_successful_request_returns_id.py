import requests
import random
import string
import pytest
from Sprint_7.data import AcceptOrder,TextOfMistake

class TestCourierRegistration:
    @staticmethod
    def generate_random_string(length):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    def setup_method(self):
        self.login = self.generate_random_string(10)
        self.password = self.generate_random_string(10)
        self.first_name = self.generate_random_string(10)
        self.payload = {
            "login": self.login,
            "password": self.password,
            "firstName": self.first_name
        }

    def test_successful_request_returns_id(self):
        response = requests.post(AcceptOrder.can_be_created_courier, data=self.payload)
        assert response.status_code == 201

        auth_payload = {"login": self.login, "password": self.password}
        response = requests.post(AcceptOrder.сourier_login, data=auth_payload)
        assert 'id' in response.json()


class TestCourierLogin:
    @staticmethod
    def generate_random_string(length):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    def setup_method(self):
        self.login = self.generate_random_string(10)
        self.password = self.generate_random_string(10)
        self.first_name = self.generate_random_string(10)
        self.payload = {
            "login": self.login,
            "password": self.password,
            "firstName": self.first_name
        }
        # Регистрируем курьера перед тестами логина
        requests.post(AcceptOrder.can_be_created_courier, data=self.payload)

    def test_courier_can_log_in(self):
        auth_payload = {"login": self.login, "password": self.password}
        response = requests.post(AcceptOrder.сourier_login, data=auth_payload)
        assert response.status_code == 200

    def test_non_existent_user(self):
        auth_payload = {"login": "nonexistent", "password": "password123"}
        response = requests.post(AcceptOrder.сourier_login, data=auth_payload)
        assert response.json()['message'] == TextOfMistake.errer_6

    def test_missing_login_field(self):
        auth_payload = {"password": self.password}
        response = requests.post(AcceptOrder.сourier_login, data=auth_payload)
        assert response.json()['code'] == 400