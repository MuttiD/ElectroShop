from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Testimonial(models.Model):
    """ Testimonial Model """

    name = models.CharField(max_length=200, default="anonymous")
    posted_date = models.DateTimeField(auto_now=True)
    delivery = models.IntegerField(
        default=1, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    quality = models.IntegerField(
        default=1, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    overall = models.IntegerField(
        default=1, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    review = models.CharField(max_length=2000, null=False, blank=False)
