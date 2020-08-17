from rest_framework import serializers
from api.models import Rentals


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rentals
        fields = ["book_id", "quantity", "duration", "rental_date"]
