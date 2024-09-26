from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from link.models import Link, Product
from link.serializers import LinkSerializer, ProductSerializer
from users.permissions import IsActive


class LinkViewSet(ModelViewSet):
    queryset = Link.objects.all
    serializer_class = LinkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']
    permission_classes = [IsActive]


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all
    serializer_class = ProductSerializer
    permission_classes = (IsActive, )


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all
    serializer_class = ProductSerializer
    permission_classes = (IsActive,)


class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all
    serializer_class = ProductSerializer
    permission_classes = (IsActive,)


class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all
    serializer_class = ProductSerializer
    permission_classes = (IsActive,)


class ProductDestroyAPIView(DestroyAPIView):
    queryset = Product.objects.all
    serializer_class = ProductSerializer
    permission_classes = (IsActive,)
