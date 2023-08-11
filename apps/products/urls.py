from django.urls import path

from apps.products.views import ProductListView, export_products_to_excel

urlpatterns = [
    path('api/products/', ProductListView.as_view(), name='products-list'),
    path('api/products/export/', export_products_to_excel, name='export-products'),

]
