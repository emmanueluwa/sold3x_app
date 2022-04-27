from django.urls import path, include
from .views import ProductList, ProductListAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('', include(router.urls)),
    path('products-filter/', ProductListAPIView.as_view()),
    path('products/', ProductList.as_view()),
]
