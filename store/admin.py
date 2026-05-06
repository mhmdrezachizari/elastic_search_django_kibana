from django.contrib import admin
from .models import Product
from .documents import ProductDocument


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price","created_at")

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        ProductDocument().update(obj)

    def delete_model(self, request, obj):
        ProductDocument().delete(obj)
        super().delete_model(request, obj)
