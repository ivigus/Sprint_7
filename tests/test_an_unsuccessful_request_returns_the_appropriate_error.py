import allure
import requests
import pytest
from data import AcceptOrder, TextOfMistake, CreateDataForUse

class TestCourierDeletion:
    """Тесты удаления курьера"""

    @pytest.fixture
    def create_courier_for_deletion(self):
        """Фикстура для создания курьера для теста удаления"""
        payload = CreateDataForUse.register_new_courier()
        create_response = requests.post(AcceptOrder.can_be_created_courier, data=payload)
        assert create_response.status_code == 201
        
        auth_payload = {"login": payload["login"], "password": payload["password"]}
        login_response = requests.post(AcceptOrder.сourier_login, data=auth_payload)
        assert login_response.status_code == 200
        courier_id = login_response.json()["id"]
        
        yield courier_id  
        
        try:
            delete_url = f"{AcceptOrder.BASE_URL}/courier/{courier_id}"
            check_response = requests.delete(delete_url)
            if check_response.status_code == 200:
                print(f"Резервное удаление курьера {courier_id}")
        except:
            pass

    @allure.title('Попытка удаления несуществующего курьера')
    def test_delete_nonexistent_courier(self):
        response = requests.delete(AcceptOrder.remove_courier_1)
        assert response.status_code == 404

    @allure.title('Попытка удаления курьера с пустым ID')
    def test_delete_with_empty_id(self):
        response = requests.delete(AcceptOrder.remove_courier_2)
        assert response.status_code == 404

    @allure.title('Успешное удаление существующего курьера')
    def test_delete_existing_courier(self, create_courier_for_deletion):
        """Удаление только что созданного курьера"""
        courier_id = create_courier_for_deletion
        delete_url = f"https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}"
        response = requests.delete(delete_url)
        print(response.json())
        assert response.status_code == 200
        assert response.json() == {"ok": True}