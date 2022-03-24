from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    model = Product
    fields = ('name', 'img', )


admin.site.register(Product, ProductAdmin)