from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from link.models import Link, Product
from link.serializers import LinkSerializer, ProductSerializer
from users.permissions import IsActive


class LinkViewSet(ModelViewSet):
    """Класс представления Звена"""

    queryset = Link.objects.all
    serializer_class = LinkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']
    permission_classes = [IsActive]


class ProductCreateAPIView(CreateAPIView):
    """Класс представления на создание Продукта"""

    queryset = Product.objects.all
    serializer_class = ProductSerializer
    permission_classes = (IsActive,)


class ProductListAPIView(ListAPIView):
    """Класс представления перечня Продукта"""

    queryset = Product.objects.all
    serializer_class = ProductSerializer
    permission_classes = (IsActive,)


class ProductRetrieveAPIView(RetrieveAPIView):
    """Класс представления единичного Продукта"""

    queryset = Product.objects.all
    serializer_class = ProductSerializer
    permission_classes = (IsActive,)


class ProductUpdateAPIView(UpdateAPIView):
    """Класс представления на редактирование Продукта"""

    queryset = Product.objects.all
    serializer_class = ProductSerializer
    permission_classes = (IsActive,)


class ProductDestroyAPIView(DestroyAPIView):
    """Класс представления на удаление Продукта"""

    queryset = Product.objects.all
    serializer_class = ProductSerializer
    permission_classes = (IsActive,)
