from django.db import models

from users.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Укажите название категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Опишите категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование продукта",
        help_text="Укажите название продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Опишите продукт",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="catalog/image",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото продукта",
    )
    owner = models.ForeignKey(
        User,
        null=True,
        blank=True,
        verbose_name="Владелец",
        on_delete=models.SET_NULL
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='category'
    )
    price_pay = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Цена за покупку",
        help_text="Введите цену"
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания записи",
        help_text="Введите дату",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата изменения записи",
        help_text="Введите дату",
        auto_now=True
    )
    manufactured_at = models.DateTimeField(
        verbose_name="Дата производства продукта",
        help_text="Введите дату",
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Опубликовано',
    )

    class Meta:
        permissions = [
            ("can_edit_category", "Can edit category"),
            ("can_edit_description", "Can edit description"),
            ("can_edit_is_published", "Can edit is_published")
        ]
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price_pay"]

    def __str__(self):
        return f'{self.name}, {self.category}'


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='product',
        verbose_name="Продукт",
    )
    num_version = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Номер версии",
        help_text="Введите номер версии"
    )
    name_version = models.CharField(
        max_length=100,
        verbose_name="Наименование версии",
        help_text="Укажите название версии",
    )
    status_version = models.BooleanField(default=True, verbose_name="Статус версии",)

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["product", "num_version"]

    def __str__(self):
        return f'{self.product}'


