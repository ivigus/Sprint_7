import requests
from Sprint_7.data import AcceptOrder

class TestCourierRegistration:
    """Тесты регистрации курьера"""

    def test_get_courier_orders(self):
        """Получение заказов курьера"""
        response = requests.get(AcceptOrder.list_of_orders)
        assert response.status_code == 200
        assert 'orders' in response.json()