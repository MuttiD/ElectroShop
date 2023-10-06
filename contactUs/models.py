from django.db import models


class ContactModel(models.Model):
    """
    A class to feature the contact page
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Contact Form {self.name} ({self.email})"
