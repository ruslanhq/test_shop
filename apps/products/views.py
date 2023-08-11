from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
