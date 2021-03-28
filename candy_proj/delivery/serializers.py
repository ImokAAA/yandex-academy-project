from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

from .models import Courier, CourierRegion, WorkingHour, Order, DeliveryHour
import datetime

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
        courier, _ = Courier.objects.get_or_create(
            courier_id = validated_data['courier_id'],
            courier_type=validated_data['courier_type'], 
            )
        courier.save()
        for region in validated_data['regions']:
            courier_region, _ = CourierRegion.objects.get_or_create(
            region = region, 
            ) 
            courier.regions.add(courier_region)
        for working_hour in validated_data['working_hours']:
            start_time_list = working_hour.split('-')[0].split(':')
            start_time = datetime.time(int(start_time_list[0]), int(start_time_list[1]))

            end_time_list = working_hour.split('-')[1].split(':')
            end_time = datetime.time(int(end_time_list[0]), int(end_time_list[1]))
            
            courier.workinghour_set.get_or_create(start_time = start_time, end_time = end_time)
            courier.save()
        return True

    def update(self, instance, validated_data):
        instance.courier_id = validated_data.get('courier_id', instance.courier_id)
        instance.courier_type = validated_data.get('courier_type', instance.courier_type)
        if validated_data.get('regions'):
            instance.regions.clear()
            instance.save()
            for region in validated_data['regions']:
                courier_region, _ = CourierRegion.objects.get_or_create(
                region = region, 
                ) 
                instance.regions.add(courier_region)
        if validated_data.get('working_hours'):
            instance.workinghour_set.all().delete()
            for working_hour in validated_data['working_hours']:
                start_time_list = working_hour.split('-')[0].split(':')
                start_time = datetime.time(int(start_time_list[0]), int(start_time_list[1]))

                end_time_list = working_hour.split('-')[1].split(':')
                end_time = datetime.time(int(end_time_list[0]), int(end_time_list[1]))
            
                instance.workinghour_set.get_or_create(start_time = start_time, end_time = end_time)
        instance.save()
        return instance


class OrderSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    weight = serializers.CharField() 
    region = serializers.IntegerField()
    delivery_hours = serializers.ListField(
        child = serializers.CharField()
        )
    
    def create(self, validated_data):
        order, _ = Order.objects.get_or_create(
            order_id = validated_data['order_id'],
            weight = validated_data['weight'],
            region = validated_data['region'], 
            )
        order.save()
        for delivery_hour in validated_data['delivery_hours']:
            start_time_list = delivery_hour.split('-')[0].split(':')
            start_time = datetime.time(int(start_time_list[0]), int(start_time_list[1]))

            end_time_list = delivery_hour.split('-')[1].split(':')
            end_time = datetime.time(int(end_time_list[0]), int(end_time_list[1]))
            
            order.deliveryhour_set.get_or_create(start_time = start_time, end_time = end_time)
            order.save()
        return True


class AssignSerializer(serializers.Serializer):
    courier_id = serializers.IntegerField()
    
    def create(self, validated_data):
        courier = Courier.objects.get(
            courier_id = validated_data['courier_id'] 
            )
        if courier.courier_type == 'foot':
            courier_max_weight = 10
        elif courier.courier_type == 'bike':
            courier_max_weight = 15
        elif courier.courier_type == 'car':
            courier_max_weight = 50
        common_orders_weight = 0
       
        if not courier.order_set.all():
            for order in Order.objects.order_by('weight'):
                region_is_common = order.region in [ region.region for region in courier.regions.all()]
                if not order.courier_id and not order.complete_time and region_is_common:
                    for working_hour in courier.workinghour_set.all():
                        for delivery_hour in order.deliveryhour_set.all():
                            time_is_common = working_hour.start_time >= delivery_hour.start_time and working_hour.start_time < delivery_hour.end_time or working_hour.end_time > delivery_hour.start_time and working_hour.end_time <= delivery_hour.end_time
                            if time_is_common:
                                order.assign_time = datetime.datetime.utcnow().isoformat()
                                order.save()
                                courier.order_set.add(order)
                                common_orders_weight += order.weight
                
                if common_orders_weight > courier_max_weight:
                    order.assign_time = None
                    courier.order_set.remove(order)
                    common_orders_weight -= order.weight
                    break 
        courier.save()
        return True


class CompleteSerializer(serializers.Serializer):
    courier_id = serializers.IntegerField()
    order_id = serializers.IntegerField()
    complete_time = serializers.CharField()

    def create(self, validated_data):
        courier = Courier.objects.get(
            courier_id = validated_data['courier_id'] 
            )
        order = Order.objects.get(
            order_id = validated_data['order_id'] 
            )
        
        order.complete_time = validated_data['complete_time']
        order.save()

        return True
    

    