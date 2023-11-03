from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """
    A Class to handle Auto Field
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
