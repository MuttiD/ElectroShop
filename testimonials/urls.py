from django.urls import path
from django.contrib import admin
from . import views
from .views import CreateTestimonial, TestimonialView



urlpatterns = [
    path('custom_admin/', admin.site.urls),
    path("", TestimonialView.as_view(), name="testimonials"),
    path(
        "create_testimonial/<int:product_id>/", CreateTestimonial.as_view(), name="create_testimonial"),
    # path('<int:product_id>/', views.product.name, name='product_name'),
        #"create/<int:product_id>/", CreateTestimonial.as_view(), name='create_testimonial'),
    # path('testimonials/create/<int:product_id>/', CreateTestimonial.as_view(), name='create_testimonial'),

]
