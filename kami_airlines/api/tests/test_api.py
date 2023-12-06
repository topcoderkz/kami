from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from api.models import Airplane
import math


class AirplaneAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_invalid_volume(self):
        data = {'volume': 0, 'passenger_assumptions': 100}
        response = self.client.post('/api/airplanes/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Volume should be more than 0.', str(response.data))

    def test_invalid_passenger_assumptions(self):
        data = {'volume': 1, 'passenger_assumptions': -50}

        # Use POST request to trigger serializer validation
        response = self.client.post('/api/airplanes/', data)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Passenger assumptions should be a non-negative integer.', str(response.data))

    def test_create_airplanes(self):
        # Test creating 10 airplanes
        for i in range(1, 11):
            response = self.client.post('/api/airplanes/', {'volume': i, 'passenger_assumptions': 100})
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if there are 10 airplanes in the database
        self.assertEqual(Airplane.objects.count(), 10)

    def test_airplane_fuel_consumption(self):
        # Assuming the calculation logic is in the view or serializer
        # This test checks if the fuel consumption is calculated correctly

        # Create an airplane
        airplane = Airplane.objects.create(volume=1, passenger_assumptions=100)

        # Calculate expected fuel consumption
        expected_consumption = math.log(airplane.volume, 10) * 0.80 + 0.002 * airplane.passenger_assumptions
        expected_max_minutes = 200 / expected_consumption

        response = self.client.get(f'/api/airplanes/{airplane.id}/')  # Assuming you have a detail endpoint

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['fuel_consumption'], expected_consumption)
        self.assertEqual(response.data['max_minutes_able_to_fly'], expected_max_minutes)
