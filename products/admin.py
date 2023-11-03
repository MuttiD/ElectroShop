from django.contrib import admin
from .models import Category, SubCategory, Product


class ProductAdmin(admin.ModelAdmin):
    """
    A Class to handle Products in Django Admin
    """
    list_display = (
        'sku',
        'name',
        'subcategory',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    A Class to handle Categories in Django Admin
    """
    list_display = (
        'friendly_name',
        'name',
    )


class SubCategoryAdmin(admin.ModelAdmin):
    """
    A Class to handle Sub Categories in Django Admin
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
