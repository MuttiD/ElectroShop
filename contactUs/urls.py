from django.urls import path
from . import views

urlpatterns = [
    path('contact_us', views.ContactView.as_view(), name="contact_us"),
    path('success', views.success, name="success"),
]
