from rest_framework import serializers

from link.models import Link, Product


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'
        read_only_fields = ['arrears']


class ProductSerializer(serializers.ModelSerializer):
    links = LinkSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
