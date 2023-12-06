from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Airplane


class AirplaneAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

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
        expected_consumption = (200 * airplane.volume) + (0.80 * airplane.volume) + (0.002 * airplane.passenger_assumptions)

        response = self.client.get(f'/api/airplanes/{airplane.volume}/')  # Assuming you have a detail endpoint

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['fuel_consumption'], expected_consumption)

    def test_max_minutes_able_to_fly(self):
        # Assuming the calculation logic is in the view or serializer
        # This test checks if the maximum minutes able to fly is calculated correctly

        # Create an airplane
        airplane = Airplane.objects.create(volume=1, passenger_assumptions=100)

        # Calculate expected maximum minutes able to fly
        expected_max_minutes = 200 / ((0.80 * airplane.volume) + (0.002 * airplane.passenger_assumptions))

        response = self.client.get(f'/api/airplanes/{airplane.volume}/')  # Assuming you have a detail endpoint

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['max_minutes_able_to_fly'], expected_max_minutes)
