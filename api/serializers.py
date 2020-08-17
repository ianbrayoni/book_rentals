from rest_framework import serializers
from api.models import Rentals


class RentalSerializer(serializers.ModelSerializer):
    book_type = serializers.ChoiceField(choices=["Regular", "Novels", "Fiction"])

    class Meta:
        model = Rentals
        fields = ["book_id", "quantity", "duration", "rental_date", "book_type"]
