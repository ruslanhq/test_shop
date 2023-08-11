from rest_framework import serializers

from apps.products.models import Product, Category, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    tags = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%SZ')

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'created_at', 'category_name', 'tags'
        ]

    def get_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]
