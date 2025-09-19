import requests
from Sprint_7.data import AcceptOrder,DataForTheTest
import pytest
class TestOrderCreation:
    """Тесты создания заказа"""
    @pytest.mark.parametrize("param", [DataForTheTest.payload, DataForTheTest.payload_1, DataForTheTest.payload_2, DataForTheTest.payload_3])
    def test_create_color_both(self,param):
        response = requests.post(AcceptOrder.create_an_order_1, json=param)
        print(response.json())
        assert response.status_code == 201
        assert 'track' in response.json()
