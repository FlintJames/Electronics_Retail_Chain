from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from link.models import Link, Product


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    """Отображение звена в административное панели"""

    list_display = ["pk", "title", "country", "city", "provider", "arrears"]
    list_filter = ["city", ]
    actions = ['clear_arrears']

    @admin.display(description="Поставщик")
    def provider(self, obj):
        url = reverse(f'admin:link_link_change', args=[obj.provider.pk])
        return format_html('<a href="{}">{}</a>', link, obj.provider)

    @admin.action(description="Обнуление долга")
    def clear_arrears(self, request, queryset):
        queryset.update(arrears=0)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Отображение продукта в административное панели"""

    list_display = ["pk", "name", "model", "release", "manufacturer"]
