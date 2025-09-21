import allure
import requests
from data import AcceptOrder

class TestCourierRegistration:
    """Тесты регистрации курьера"""

    @allure.title('Получение списка заказов для конкретного курьера')
    def test_get_courier_orders(self):
        """Получение заказов курьера"""
        response = requests.get(AcceptOrder.list_of_orders)
        assert response.status_code == 200
        assert 'orders' in response.json()