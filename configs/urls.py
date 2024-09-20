from django.urls import path
from cars_app.views import Cars, CarsRetrive

urlpatterns = [
    path('cars', Cars.as_view(), name='cars_app'),
    path('cars/<int:pk>', CarsRetrive.as_view(), name='cars_app/retrive')
]
