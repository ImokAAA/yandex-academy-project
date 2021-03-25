from django.urls import path
from .views import CourierList, CourierDetail

app_name = "delivery"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('couriers', CourierList.as_view()),
    path('couriers/<int:pk>', CourierDetail.as_view()),
]