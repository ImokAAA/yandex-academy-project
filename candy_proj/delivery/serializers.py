from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

from .models import Courier

class CourierSerializer(serializers.Serializer):
    courier_id = serializers.IntegerField()
    courier_type = serializers.CharField() 
    regions = serializers.ListField(
        child = serializers.IntegerField()
        )
    working_hours = serializers.ListField(
        child = serializers.CharField()
        )
    
    def create(self, validated_data):
        print("validated data: " + str(validated_data))
        return True
        #return Courier.objects.create(**validated_data)