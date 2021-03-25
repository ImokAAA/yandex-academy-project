from .models import Courier
from .serializers import CourierSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CourierList(APIView):
    """
    Create new couriers.
    """

    def post(self, request):
        couriers = request.data.get('data')
        serializer = CourierSerializer(data=couriers, many = True)
        couriers_id = []
        if serializer.is_valid():
            serializer.save()
            for courier in couriers:
                couriers_id.append({"id": courier['courier_id']})
            return Response({"couriers": couriers_id}, status=status.HTTP_201_CREATED)
        for i in range(len(couriers)):
            if serializer.errors[i]:
                couriers_id.append({"id": couriers[i]['courier_id']})
        return Response({"validation_error": {"couriers": couriers_id}}, status=status.HTTP_400_BAD_REQUEST, )
