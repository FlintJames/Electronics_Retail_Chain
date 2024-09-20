from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Link(models.Model):
    FACTORY = "factory"
    RETAIL = "retail"
    INDIVIDUAL_ENTREPRENEUR = "individual_entrepreneur"
    STRUCTURE = [
        (FACTORY, "Завод"),
        (RETAIL, "Розничная сеть"),
        (INDIVIDUAL_ENTREPRENEUR, "Индивидуальный предприниматель"),
    ]

    title = models.CharField(max_length=100, verbose_name="Название")

    email = models.EmailField(max_length=100, unique=True, verbose_name="Электронная почта")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house_number = models.CharField(max_length=100, verbose_name="Номер дома")

    structure = models.CharField(max_length=50, choices=STRUCTURE, verbose_name="Структура")
    provider = models.ForeignKey("self", on_delete=models.SET_NULL, **NULLABLE, verbose_name="Поставщик")

    arrears = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Задолженность")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    owner = models.ForeignKey(User, default=True, on_delete=models.CASCADE, verbose_name="Владелец")

    def str(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Звено"
        verbose_name_plural = "Звенья"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    model = models.CharField(max_length=150, verbose_name="Модель")
    release = models.DateField(verbose_name="Дата выхода")

    manufacturer = models.ForeignKey(Link, on_delete=models.CASCADE, verbose_name="Производитель")

    def str(self):
        return f"{self.name} ({self.model})"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
