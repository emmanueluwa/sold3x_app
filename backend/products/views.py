# https://www.django-rest-framework.org/tutorial/3-class-based-views/

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response

class ProductList(APIView):
    # list products
    def get(self, request):
        products = Product.object.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductListAPIView(ListAPIView):
        serializer_class = ProductSerializer
        queryset = Product.objects.all()

        #using search bar in frontned
        search_fields = (
            'title'
        )
