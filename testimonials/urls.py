from django.urls import path
from . import views
from .views import CreateTestimonial



urlpatterns = [
    path("", views.TestimonialView.as_view(), name="testimonials"),
    path(
        "create_testimonial/<int:product_id>/", views.CreateTestimonial.as_view(), name="create_testimonial"),
        #"create/<int:product_id>/", CreateTestimonial.as_view(), name='create_testimonial'),
    # path('testimonials/create/<int:product_id>/', CreateTestimonial.as_view(), name='create_testimonial'),

]
