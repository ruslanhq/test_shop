from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from apps.products.models import Product
from apps.products.serializers import ProductSerializer
from apps.products.services import export_products_to_excel


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def export_products(request):
    products = Product.objects.all()
    return export_products_to_excel(products)
