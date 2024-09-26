from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from link.models import Link, Product


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "country", "city", "provider", "arrears"]
    list_filter = ["city", ]
    actions = ['clear_arrears']

    @admin.display(description="Поставщик")
    def provider(self, obj):
        url = reverse(f'admin:link_link_change', args=[obj.provider.pk])
        return mark_safe(f'<a href="{url}">{obj.provider}</a>')

    @admin.action(description="Обнуление долга")
    def clear_arrears(self, request, queryset):
        queryset.update(arrears=0)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "model", "release", "manufacturer"]
