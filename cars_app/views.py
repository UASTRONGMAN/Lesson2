from rest_framework.views import APIView
from cars_app.models import carModel
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework import status

class Cars(APIView):
    def get(self, *args, **kwargs):
        cars = carModel.objects.all()
        cars = [model_to_dict(car) for car in cars]
        return Response(cars, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        car = carModel.objects.create(**data)
        return Response(model_to_dict(car), status=status.HTTP_201_CREATED)


class CarsRetrive(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = carModel.objects.get(pk=pk)
        except carModel.DoesNotExist:
            return Response('not found', status=status.HTTP_404_NOT_FOUND)
        return Response(model_to_dict(car), status=status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data
        try:
            car = carModel.objects.get(pk=pk)
        except carModel.DoesNotExist:
            return Response('not found', status=status.HTTP_404_NOT_FOUND)
        car.model = data['model']
        car.price = data['price']
        car.year = data['year']
        car.save()
        return Response(model_to_dict(car), status=status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        return Response("Hello World")

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            carModel.objects.get(pk=pk).delete()
        except carModel.DoesNotExist:
            return Response('not found', status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)