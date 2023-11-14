from django.db import models
from products.models import Product


CHOICES = ((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"))


class Testimonial(models.Model):
    """ A class to handle Testimonials """

    name = models.CharField(max_length=200,
                            default="type your name")
    posted_date = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='testimonials')

    delivery = models.IntegerField(
        default=1, choices=CHOICES
    )
    quality = models.IntegerField(
        default=1, choices=CHOICES
    )
    overall = models.IntegerField(
        default=1, choices=CHOICES
    )
    review = models.CharField(max_length=2000,
                              null=False, blank=False)
