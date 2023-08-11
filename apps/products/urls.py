from django.urls import path

from apps.products.views import ProductListView

urlpatterns = [
    path('api/products/', ProductListView.as_view(), name='products-list'),
]
