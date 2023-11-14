from django.urls import path
from django.contrib import admin
from . import views
from .views import CreateTestimonial, TestimonialView

urlpatterns = [
    path("", TestimonialView.as_view(), name="testimonials"),
    path(
         "create_testimonial/<int:product_id>/",
         CreateTestimonial.as_view(), name="create_testimonial"),
]
