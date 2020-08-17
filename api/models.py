from django.db import models


class Invoices(models.Model):
    id = models.UUIDField(primary_key=True, null=False)
    date_generated = models.DateTimeField(null=False)
    total_charges = models.DecimalField(null=False, max_digits=12, decimal_places=2)


class Rentals(models.Model):
    book_id = models.IntegerField(null=False)
    invoice = models.ForeignKey(Invoices, on_delete=models.CASCADE)
    duration = models.IntegerField(null=False)
    quantity = models.IntegerField(null=False)
    rental_date = models.DateTimeField(null=False)
    charge = models.DecimalField(null=False, max_digits=12, decimal_places=2)
