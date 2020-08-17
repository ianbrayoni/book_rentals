import json
from django.test import TestCase
from rest_framework.test import APIClient
from django.conf import settings


class TestRentalView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + settings.API_KEY)
        self.endpoint = "/api/v1/rentals"
        self.payload = [
            {
                "bookId": 1,
                "quantity": 2,
                "rentalDate": "2020-08-15T12:12:59.785466",
                "duration": 3,
            }
        ]

    def test_post_rental_resource_created(self):
        response = self.client.post(self.endpoint, self.payload, format="json")
        self.assertTrue(response.status_code == 201)
        statement = json.loads(response.content)
        self.assertEquals(
            statement,
            {
                "invoiceId": statement["invoiceId"],
                "totalCharges": 6,
                "charges": [{"bookId": 1, "charge": 6}],
            },
        )

    def test_post_rental_no_payload_error(self):
        response = self.client.post(self.endpoint, [], format="json")
        self.assertTrue(response.status_code == 400)

    def test_post_rental_incorrect_payload(self):
        # Example: bookId not provided in payload
        payload = [
            {"quantity": 2, "rentalDate": "2020-08-15T12:12:59.785466", "duration": 3}
        ]
        response = self.client.post(self.endpoint, payload, format="json")
        self.assertTrue(response.status_code == 400)
        self.assertEquals(
            json.loads(response.content),
            {"errorMessage": {"bookId": ["This field is required."]}},
        )

    def test_post_rental_no_auth_forbidden(self):
        self.client.credentials()
        response = self.client.post(self.endpoint, self.payload, format="json")
        self.assertTrue(response.status_code == 403)
