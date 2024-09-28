from rest_framework import serializers

from link.models import Link, Product


class LinkSerializer(serializers.ModelSerializer):
    """Обработка модели Звена"""

    class Meta:
        model = Link
        fields = '__all__'
        read_only_fields = ['arrears']


class ProductSerializer(serializers.ModelSerializer):
    """Обработка модели Продукт"""

    links = LinkSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
