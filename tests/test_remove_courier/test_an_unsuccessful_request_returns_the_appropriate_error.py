import requests
from Sprint_7.data import AcceptOrder

class TestCourierDeletion:
    """Тесты удаления курьера"""

    def test_delete_nonexistent_courier(self):
        response = requests.delete(AcceptOrder.remove_courier_1)
        assert response.status_code == 404

    def test_delete_with_empty_id(self):
        response = requests.delete(AcceptOrder.remove_courier_2)
        assert response.status_code == 404

    def test_delete_existing_courier(self):
        response = requests.delete(AcceptOrder.remove_courier_3)
        print(response.json())
        assert response.status_code == 200