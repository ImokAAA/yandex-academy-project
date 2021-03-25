from django.urls import path
from .views import CourierList

app_name = "delivery"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('couriers', CourierList.as_view()),
    path('couriers/<int:pk>', CourierList.as_view()),
]