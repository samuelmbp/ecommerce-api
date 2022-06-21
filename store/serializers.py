from decimal import Decimal
from rest_framework import serializers

from store.models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']

    # products_count = serializers.SerializerMethodField(
    #     method_name='count_products'
    # )

    # def count_products(self, product):
    #     return product.featured_product.inventory


class ProductSerializer(serializers.ModelSerializer):
    # ModelSerializer -> rest-framework(avoids fields repetition)
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory',
                  'unit_price', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
