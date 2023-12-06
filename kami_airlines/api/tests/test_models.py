from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Airplane


class AirplaneAPITestCase(APITestCase):
    def setUp(self):
        # Create an airplane for testing detail and update
        self.airplane = Airplane.objects.create(volume=1, passenger_assumptions=100)

    def test_get_airplane_detail(self):
        response = self.client.get(f'/api/airplanes/{self.airplane.volume}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['volume'], self.airplane.volume)

    def test_update_airplane(self):
        data = {'volume': 1, 'passenger_assumptions': 150}  # Include 'volume' in the data
        response = self.client.put(f'/api/airplanes/{self.airplane.volume}/', data)
        
        if response.status_code != status.HTTP_200_OK:
            print(response.data)  # Add this line to print details of the response
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.airplane.refresh_from_db()
        self.assertEqual(self.airplane.passenger_assumptions, 150)
