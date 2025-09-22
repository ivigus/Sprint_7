import allure
import requests
from data import AcceptOrder, TextOfMistake

class TestOrderAcceptance:
    """Тесты принятия заказов"""

    @allure.title('Получение ошибки при запросе несуществующего заказа')
    def test_order_not_found(self):
        """Проверка ошибки при несуществующем заказе"""
        response = requests.get(AcceptOrder.order_not_found_1)
        assert response.json()['message'] == TextOfMistake.error_5

    @allure.title('Получение ошибки при отсутствии номера трека в запросе')
    def test_missing_track_number(self):
        """Проверка ошибки при отсутствии номера заказа"""
        response = requests.get(AcceptOrder.order_not_found_2)
        assert response.json()['message'] == TextOfMistake.error_3

    @allure.title('Успешное получение информации о заказе по номеру трека')
    def test_successful_order_tracking(self):
        """Проверка успешного получения заказа"""
        response = requests.get(AcceptOrder.order_not_found_3)
        assert 'order' in response.json()