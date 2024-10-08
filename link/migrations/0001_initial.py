# Generated by Django 4.2.2 on 2024-09-20 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Link",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="Название")),
                (
                    "email",
                    models.EmailField(
                        max_length=100, unique=True, verbose_name="Электронная почта"
                    ),
                ),
                ("country", models.CharField(max_length=100, verbose_name="Страна")),
                ("city", models.CharField(max_length=100, verbose_name="Город")),
                ("street", models.CharField(max_length=100, verbose_name="Улица")),
                (
                    "house_number",
                    models.CharField(max_length=100, verbose_name="Номер дома"),
                ),
                (
                    "structure",
                    models.CharField(
                        choices=[
                            ("factory", "Завод"),
                            ("retail", "Розничная сеть"),
                            (
                                "individual_entrepreneur",
                                "Индивидуальный предприниматель",
                            ),
                        ],
                        max_length=50,
                        verbose_name="Структура",
                    ),
                ),
                (
                    "arrears",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=12,
                        verbose_name="Задолженность",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
            ],
            options={
                "verbose_name": "Звено",
                "verbose_name_plural": "Звенья",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                ("model", models.CharField(max_length=150, verbose_name="Модель")),
                ("release", models.DateField(verbose_name="Дата выхода")),
                (
                    "manufacturer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="link.link",
                        verbose_name="Производитель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
