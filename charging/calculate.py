import uuid
from datetime import datetime
from django.conf import settings

from api.models import Rentals, Invoices
from utils.helpers import error_handler


class Charges:
    """
    Calculate charges for books rented
    """

    def __init__(self, rental=[]):
        self.rental = rental

    def _calculate_charge(self, quantity, book_type, duration):
        return quantity * self.CHARGES[book_type] * duration

    @error_handler
    def calculate(self):
        invoice_id = uuid.uuid4()
        total_charges = 0
        statement = dict(invoiceId=invoice_id, totalCharges=total_charges, charges=[])

        # create invoice instance
        invoice = Invoices(
            id=invoice_id,
            total_charges=total_charges,
            date_generated=datetime.now().isoformat(),
        )
        invoice.save()

        for data in self.rental:
            charge = self._calculate_charge(
                data["quantity"], data["book_type"], data["duration"]
            )

            charges_per_book = dict(bookId=data["book_id"], charge=charge)
            statement["charges"].append(charges_per_book)

            rental = Rentals(
                book_id=data["book_id"],
                invoice=invoice,
                duration=data["duration"],
                quantity=data["quantity"],
                rental_date=data["rental_date"],
                charge=charge,
            )
            rental.save()

            total_charges += charge

        # update total_charges in Invoice
        invoice.total_charges = total_charges
        invoice.save()

        statement["totalCharges"] = total_charges

        return statement
