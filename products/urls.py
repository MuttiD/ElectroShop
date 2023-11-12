from django.urls import path
from . import views
from testimonials.views import CreateTestimonial, TestimonialView

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('add_comment/<int:product_id>/', views.add_comment, name='add_comment'),
    path('update_comment/<int:comment_id>/', views.update_comment, name='update_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('create_testimonial/<int:product_id>/', CreateTestimonial.as_view(), name='create_testimonial'),
    path('testimonials/<int:product_id>/', TestimonialView.as_view(), name='testimonials'),

]
