from .models import Courier, Order
from .serializers import CourierSerializer, OrderSerializer, AssignSerializer, CompleteSerializer
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


class CourierDetail(APIView):
    """
    Retrieve, update a courier instance.
    """
    def get_object(self, pk):
        try:
            return Courier.objects.get(courier_id=pk)
        except Courier.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = CourierSerializer(snippet)
        return Response(serializer.data)

    def patch(self, request, pk):
        courier = self.get_object(pk)
        couriers = request.data.get('regions')
        serializer = CourierSerializer(courier, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            courier = self.get_object(pk)
            regions = [region.region for region in courier.regions.all()]
            working_hours = [str(working_hour.start_time.strftime("%H:%M")) + "-" + str(working_hour.end_time.strftime("%H:%M")) for working_hour in courier.workinghour_set.all()]
            courier_dic = {
                "courier_id": courier.courier_id,
                "courier_type": courier.courier_type,
                "regions": regions,
                "working_hours": working_hours
                }
            
            return Response(courier_dic)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class OrderList(APIView):
    """
    Create new orders.
    """

    def post(self, request):
        orders = request.data.get('data')
        serializer = OrderSerializer(data=orders, many = True)
        orders_id = []
        if serializer.is_valid():
            serializer.save()
            for order in orders:
                orders_id.append({"id": order['order_id']})
            return Response({"orders": orders_id}, status=status.HTTP_201_CREATED)
        for i in range(len(orders)):
            if serializer.errors[i]:
                orders_id.append({"id": orders[i]['order_id']})
        return Response({"validation_error": {"orders": orders_id}}, status=status.HTTP_400_BAD_REQUEST, )


class AssignOrder(APIView):
    """
    This class assigns orders to courier
    """

    def post(self, request):
        serializer = AssignSerializer(data=request.data)
        orders_id = []
        try:
            courier = Courier.objects.get(
                courier_id = request.data['courier_id'] 
                )
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST )    
        if serializer.is_valid():
            if serializer.save():
                for order in courier.order_set.all():
                    assign_time = order.assign_time
                    orders_id.append({"id": order.order_id})
                return Response({"orders": orders_id, "assign_time": assign_time }, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST )


class CompleteOrder(APIView):
    """
    This class completes order of courier
    """
    def post(self, request):
        serializer = CompleteSerializer(data=request.data)
        try:
            courier = Courier.objects.get(
                courier_id = request.data['courier_id'] 
                )
            order = Order.objects.get(
                order_id = request.data['order_id'] 
                )
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST )

        if courier.courier_id == order.courier_id and order.assign_time:
            if serializer.is_valid():
                if serializer.save():
                    return Response({"order_id": order.order_id}, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST )
        return Response(status=status.HTTP_400_BAD_REQUEST )