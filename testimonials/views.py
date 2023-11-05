from django.views.generic import ListView, CreateView
from .models import Testimonial
from .forms import TestimonialForm
from django.contrib.messages.views import SuccessMessageMixin


class TestimonialView(ListView):
    """ A class to a list of Testimonials """
    template_name = "testimonials/testimonial.html"
    model = Testimonial
    context_object_name = "testimonials"


class CreateTestimonial(SuccessMessageMixin, CreateView):
    """ A class to handle success on creating Testimonials """
    template_name = "testimonials/create_testimonial.html"
    model = Testimonial
    form_class = TestimonialForm
    success_url = "/"
    success_message = "testimonial created successfully"
