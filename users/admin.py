from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Отображение пользователя в административной панели"""

    list_display = ['pk', 'email', 'is_active', 'is_staff', 'is_superuser']
