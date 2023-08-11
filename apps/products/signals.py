from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.core.cache import cache

from apps.products.models import Product


@receiver([post_save, post_delete], sender=Product)
def invalidate_product_cache(sender, instance, **kwargs):
    cache.delete('product_list')
