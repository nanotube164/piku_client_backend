from django.shortcuts import render
from .models import Product
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ProductSerializer
# Create your views here.

class ProductViewSet(viewsets.ViewSet):
    def list(selfself, request): #/api/products
        # products = Product.objects.all()
        # serializer = ProductSerializer(products, many=True)
        # # publish()
        # return Response(serializer.data)
        return Response("hello")

    # def like(id):  # /api/products/<int:id>/like
    #     req = requests.get('http://docker.for.mac.localhost:8000/api/user')
    #     json = req.json()
    #
    #     try:
    #         productUser = ProductUser(user_id=json['id'], product_id=id)
    #         productUser.save()
    #
    #         # event
    #         # publish()
    #         print('test')
    #     except:
    #         return HttpResponseBadRequest('You already liked this product')
    #
    #     return Response(serializer.data, status=status.HTTP_202_ACCEPTED)