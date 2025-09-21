import allure
import requests
from data import AcceptOrder, TextOfMistake, DataForTheTest

class TestOrderAcceptance:
    """Тесты принятия заказов курьером"""

    @allure.title('Попытка принять несуществующий заказ')
    def test_nonexistent_order(self):
        """Попытка принять несуществующий заказ"""
        response = requests.put(AcceptOrder.Url_accept_order_1)
        assert response.json()['message'] == TextOfMistake.error_1

    @allure.title('Попытка принять заказ несуществующим курьером')
    def test_nonexistent_courier(self):
        """Попытка принять заказ несуществующим курьером"""
        response = requests.put(AcceptOrder.Url_accept_order_2)
        assert response.json()['message'] == TextOfMistake.error_2

    @allure.title('Попытка принять заказ с несуществующим ID курьера')
    def test_nonexistent_courier_id(self):
        """Попытка принять заказ с несуществующим ID курьера"""
        response = requests.put(AcceptOrder.Url_accept_order_3)
        assert response.json()['message'] == TextOfMistake.error_2 

    @allure.title('Попытка принять заказ без указания всех параметров')
    def test_missing_parameters(self):
        """Попытка принять заказ без указания всех параметров"""
        response = requests.put(AcceptOrder.Url_accept_order_4)
        assert response.json()['message'] == TextOfMistake.error_3

    @allure.title('Успешное принятие заказа существующим курьером')
    def test_successful_order_acceptance(self):
        """Успешное принятие заказа"""
        create_response = requests.post(AcceptOrder.create_an_order_1, json=DataForTheTest.payload)
        assert create_response.status_code == 201
        track_number = create_response.json()['track']
        
        get_id_response = requests.get(f"https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t={track_number}")
        assert get_id_response.status_code == 200
        order_id = get_id_response.json()['order']['id']
        
        response = requests.put(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/{order_id}?courierId=585596')
        assert response.json() == {"ok": True}