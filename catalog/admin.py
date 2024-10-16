from django.contrib import admin
from django.contrib.admin import ModelAdmin

from catalog.models import Category, Product, Version


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price_pay", "category")
    list_filter = ("category", )
    search_fields = ("name", "description",)


@admin.register(Version)
class VersionAdmin(ModelAdmin):
    list_display = ("id", "product", "name_version", "num_version", "status_version")
    list_filter = ("product",)
    search_fields = ("product", "num_version",)


