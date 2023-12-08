from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Airplane


class AirplaneTestCase(APITestCase):
    def setUp(self):
        # Create an airplane for testing detail and update
        self.airplane = Airplane.objects.create(
            volume=1, passenger_assumptions=100)

    def test_get_airplane_detail(self):
        response = self.client.get(f"/api/airplanes/{self.airplane.volume}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["volume"], self.airplane.volume)

    def test_update_airplane(self):
        # Include 'volume' in the data
        data = {"volume": 1, "passenger_assumptions": 150}
        response = self.client.put(
            f"/api/airplanes/{self.airplane.volume}/", data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.airplane.refresh_from_db()
        self.assertEqual(self.airplane.passenger_assumptions, 150)
