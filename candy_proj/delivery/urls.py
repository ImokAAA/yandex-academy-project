from django.urls import path
from .views import CourierList, CourierDetail, OrderList, AssignOrder

app_name = "delivery"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('couriers', CourierList.as_view()),
    path('couriers/<int:pk>', CourierDetail.as_view()),
    path('orders', OrderList.as_view()),
    path('orders/assign', AssignOrder.as_view()),
]