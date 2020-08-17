from django.test import TestCase

from .calculate import Charges
from api.models import Rentals, Invoices


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
                "totalCharges": 22.5,
                "charges": [
                    {"bookId": 1, "charge": 9},
                    {"bookId": 2, "charge": 1.5},
                    {"bookId": 3, "charge": 12},
                ],
            },
        )
