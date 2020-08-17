from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import RentalSerializer
from .permissions import APIAuthentication
from .models import Rentals
from charging.calculate import Charges
from utils.helpers import underlize, camelize


class Rentals(APIView):
    permission_classes = [
        APIAuthentication,
    ]

    def post(self, request):
        if not request.data:
            return Response(
                {"errorMessage": "Request Body cannot be Null"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # jsonschema to snake_case: underlize keys
        data = [{underlize(k): v for k, v in data.items()} for data in request.data]

        for d in data:
            serializer = RentalSerializer(data=d)
            if not serializer.is_valid():
                # jsonschema: camelize keys
                errors = {camelize(k, False): v for k, v in serializer.errors.items()}
                return Response(
                    {"errorMessage": errors}, status=status.HTTP_400_BAD_REQUEST
                )

        statement = Charges(rental=data).calculate()
        return Response(statement, status=status.HTTP_201_CREATED)
