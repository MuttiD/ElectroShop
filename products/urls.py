from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('add_comment/<int:product_id>/', views.add_comment, name='add_comment'),
    path('update_comment/<int:comment_id>/', views.update_comment, name='update_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
