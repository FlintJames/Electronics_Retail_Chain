from django.urls import path
from rest_framework.routers import DefaultRouter

from link.apps import LinkConfig
from link.views import LinkViewSet, ProductCreateAPIView, ProductRetrieveAPIView, ProductListAPIView, \
    ProductUpdateAPIView, ProductDestroyAPIView

app_name = LinkConfig.name

router = DefaultRouter()
router.register("links", LinkViewSet, basename="links")

urlpatterns = [
    path("product/", ProductListAPIView.as_view(), name="product_list"),
    path("product/<int:pk>/", ProductRetrieveAPIView.as_view(), name="product_retrieve"),
    path("product/create/", ProductCreateAPIView.as_view(), name="product_create"),
    path("product/<int:pk>/delete/", ProductDestroyAPIView.as_view(), name="product_delete"),
    path("product/<int:pk>/update/", ProductUpdateAPIView.as_view(), name="product_update")
]

urlpatterns += router.urls
