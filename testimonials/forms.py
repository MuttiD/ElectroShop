from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    """ Form to create Testimonial """
    class Meta:
        model = Testimonial
        fields = ['name', 'delivery', 'quality', 'overall', 'review']

    labels = {
        'name': 'Your Name',
        'delivery': 'Delivery Rating',
        'quality': 'Quality Rating',
        'overall': 'Overall Rating',
        'review': 'Your Testimonial',
    }

