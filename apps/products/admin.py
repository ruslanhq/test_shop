from django.contrib import admin

from apps.products.models import Product, Tag, Category

admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Category)
