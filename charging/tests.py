from django.test import TestCase

from .calculate import Charges
from api.models import Rentals, Invoices
from .book import Regular, Fiction, Novels


class CalculateTestCase(TestCase):
    def setUp(self):
        self.rental = [
            {
                "book_id": 1,
                "quantity": 2,
                "rental_date": "2020-08-15T12:12:59.785466",
                "duration": 3,
                "book_type": "Regular",
            },
            {
                "book_id": 2,
                "quantity": 1,
                "rental_date": "2020-08-15T12:12:59.785466",
                "duration": 1,
                "book_type": "Novels",
            },
            {
                "book_id": 3,
                "quantity": 1,
                "rental_date": "2020-08-15T12:12:59.785466",
                "duration": 4,
                "book_type": "Fiction",
            },
        ]
        self.statement = Charges(rental=self.rental).calculate()

    def test_invoice_and_rentals_records_created(self):
        invoices = Invoices.objects.all()
        rental_records = Rentals.objects.filter(invoice=invoices[0].id)
        # one invoice is created for all 3 rentals
        self.assertTrue(invoices.count() == 1)
        self.assertTrue(rental_records.count() == 3)

    def test_statement_created(self):
        self.assertDictEqual(
            self.statement,
            {
                "invoiceId": self.statement["invoiceId"],
                "totalCharges": 23.5,
                "charges": [
                    {"bookId": 1, "charge": 7},
                    {"bookId": 2, "charge": 4.5},
                    {"bookId": 3, "charge": 12},
                ],
            },
        )


class CalculateBookTestCase(TestCase):
    def test_regular_books_minimum_duration_charge(self):
        charge = Regular().cost_to_rent(1, 1)
        self.assertTrue(charge == 2)

    def test_regular_books_above_minimum_duration_charge(self):
        charge = Regular().cost_to_rent(1, 5)
        self.assertTrue(charge == 6.5)

    def test_novels_books_minimum_duration_charge(self):
        charge = Novels().cost_to_rent(1, 2)
        self.assertTrue(charge == 4.5)

    def test_novels_books_above_minimum_duration_charge(self):
        charge = Novels().cost_to_rent(1, 6)
        self.assertTrue(charge == 9)

    def test_fiction_books_charge(self):
        charge = Fiction().cost_to_rent(1, 5)
        self.assertTrue(charge == 15)
