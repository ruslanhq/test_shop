from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from django.core.cache import cache

from apps.products.models import Product
from apps.products.serializers import ProductSerializer
from apps.products.services import export_products_to_excel


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.select_related('category').prefetch_related('tags')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        cache_key = 'product_list'
        try:
            cached_data = cache.get(cache_key)
        except Exception as e:
            cached_data = None
            print(e)  # TODO add Logger

        if cached_data is None:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            try:
                cache.set(cache_key, serializer.data)
            except Exception as e:
                print(e)  # TODO add Logger

            return Response(serializer.data)

        return Response(cached_data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def export_products(request):
    products = Product.objects.all()
    return export_products_to_excel(products)
