import requests
from Sprint_7.data  import AcceptOrder,TextOfMistake

class TestOrderAcceptance:
    """Тесты принятия заказов курьером"""

    def test_nonexistent_order(self):
        """Попытка принять несуществующий заказ"""
        response = requests.put(AcceptOrder.Url_accept_order_1)
        assert response.json()['message'] == TextOfMistake.errer_1

    def test_nonexistent_courier(self):
        """Попытка принять заказ несуществующим курьером"""
        response = requests.put(AcceptOrder.Url_accept_order_2)
        assert response.json()['message'] == TextOfMistake.errer_2

    def test_missing_parameters(self):
        """Попытка принять заказ без указания всех параметров"""
        response = requests.put(AcceptOrder.Url_accept_order_3)
        assert response.json()['message'] == TextOfMistake.errer_3

    def test_empty_courier_id(self):
        """Попытка принять заказ с пустым ID курьера"""
        response = requests.put(AcceptOrder.Url_accept_order_4)
        assert response.json()['message'] == TextOfMistake.errer_3

    def test_successful_order_acceptance(self):
        """Успешное принятие заказа"""
        get_id_response = requests.get(AcceptOrder.Url_accept_order_5)
        id = get_id_response.json()['order']['id']
        response = requests.put(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/{id}?courierId=585596')
        assert response.json() == {"ok": True}