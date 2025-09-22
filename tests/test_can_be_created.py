import allure
import requests
import pytest
from data import AcceptOrder, TextOfMistake, CreateDataForUse

class TestCourierRegistration:
    """Тесты регистрации курьера"""

    def _delete_courier(self, login, password):
        """Вспомогательный метод для удаления курьера"""
        try:
            auth_payload = {"login": login, "password": password}
            login_response = requests.post(AcceptOrder.сourier_login, data=auth_payload)
            
            if login_response.status_code == 200:
                courier_id = login_response.json()["id"]
                base_url = "https://qa-scooter.praktikum-services.ru/api/v1"
                delete_url = f"{base_url}/courier/{courier_id}"
                delete_response = requests.delete(delete_url)
                print(f"Удален курьер {login}: статус {delete_response.status_code}")
        except Exception as e:
            print(f"Ошибка при удалении курьера {login}: {e}")

    @pytest.fixture
    def create_courier_fixture(self):
        """Фикстура для создания и удаления курьера"""
        payload = CreateDataForUse.register_new_courier()
        response = requests.post(AcceptOrder.can_be_created_courier, data=payload)
        assert response.status_code == 201
        assert response.json() == {'ok': True}
        
        yield payload  
        
        self._delete_courier(payload["login"], payload["password"])

    @allure.title('Регистрация нового курьера и проверка возвращаемых данных')
    def test_register_new_courier_and_check_data(self, create_courier_fixture):
        """Регистрация нового курьера и проверка данных"""
        payload = create_courier_fixture
        print(f"Создан курьер: {payload['login']}")

    @allure.title('Успешная регистрация курьера возвращает статус OK')
    def test_successful_request_returns_valid_data(self, create_courier_fixture):
        """Успешная регистрация возвращает корректные данные"""
        payload = create_courier_fixture
        assert payload["login"]  

    @allure.title('Проверка ошибки при регистрации курьера без логина')
    def test_all_required_fields_no_login(self):
        """Проверка обязательности поля login"""
        payload = CreateDataForUse.register_new_courier()
        del payload["login"]

        response = requests.post(AcceptOrder.can_be_created_courier, data=payload)
        assert response.json()['message'] == TextOfMistake.error_4

    @allure.title('Проверка ошибки при регистрации курьера без пароля')
    def test_all_required_fields_no_pass(self):
        """Проверка обязательности поля password"""
        payload = CreateDataForUse.register_new_courier()
        del payload["password"] 

        response = requests.post(AcceptOrder.can_be_created_courier, data=payload)
        assert response.json()['message'] == TextOfMistake.error_4

    @allure.title('Проверка кода 201 при успешной регистрации курьера')
    def test_register_new_courier_status_code(self, create_courier_fixture):
        """Проверка кода ответа при регистрации"""
        payload = create_courier_fixture
        assert True

    @pytest.fixture
    def create_duplicate_courier_fixture(self):
        """Фикстура для теста с дубликатом курьера"""
        login = f'sanek_{pytest.current_test_name}_{pytest.config.option.verbose}'
        password = '12345'
        first_name = 'sanek15'

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response1 = requests.post(AcceptOrder.can_be_created_courier, data=payload)
        assert response1.status_code == 201
        
        yield payload 
        
        self._delete_courier(login, password)

    @allure.title('Проверка ошибки при создании дубликата курьера')
    def test_cannot_create_identical_couriers(self):
        """Проверка создания дубликатов курьеров"""
        payload = CreateDataForUse.register_new_courier()
        response1 = requests.post(AcceptOrder.can_be_created_courier, data=payload)
        assert response1.status_code == 201
        
        response2 = requests.post(AcceptOrder.can_be_created_courier, data=payload)
        assert response2.status_code == 409
        
        self._delete_courier(payload["login"], payload["password"])