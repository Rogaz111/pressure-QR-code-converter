from datetime import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import make_aware
from my_app.models import PressureReading


# Creating two test cases to demonstrate Unit Testing ability

#Testing Model initialization and object creation via ORM
class PressureReadingModelTest(TestCase):
    def setUp(self):
        # Sample PressureReading instance

        # Test gave warning for non-timezone-aware object passed for the below value for capture_date
        # capture_date="2024-03-15 08:30:00"

        # Added the below wrapper to address the warning
        capture_date = make_aware(datetime(2024, 3, 15, 8, 30))

        PressureReading.objects.create(
            sample_number="S010",
            fruit_type="apple",
            reading_1=25.89,
            reading_2=26.50,
            capture_date=capture_date,
            sample_status="I",
            capture_station="Station_1"
        )

    def test_pressure_reading_creation(self):
        # Check if the instance is created successfully - Queries Specific Record
        reading = PressureReading.objects.get(sample_number="S010")
        # Check if the Fruit Type field is Equal to Apple
        self.assertEqual(reading.fruit_type, "apple", "Fruit Type value test did not pass")
        # Check if the Status field is Equal to I
        self.assertEqual(reading.sample_status, "I", "Sample Status value test did not pass")


# Check if View Import route is accessible and using the correct template
class ImportViewTest(TestCase):
    def test_import_view_page_loads(self):
        # Send a GET request to the import_view
        response = self.client.get(reverse('imports'))
        print(response.status_code)
        print(response)

        # Assert that the response returns a 200 OK status
        self.assertEqual(response.status_code, 200, "The import_view page did not load successfully.")

        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'my_app/imports.html', "The import_view did not render the correct template.")
