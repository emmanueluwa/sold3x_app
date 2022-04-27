from rest_framework.serializers import ModelSerializer
from .models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = (
          'thumbnail',
          'url',
          'title'
          'condition',
          'price',
          'sold_time',
          'listing_type',
        )
