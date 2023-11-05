from django.urls import path
from . import views


urlpatterns = [
    path("", views.TestimonialView.as_view(), name="testimonials"),
    path(
        "create/", views.CreateTestimonial.as_view(), name="create_testimonial"
    ),
]
